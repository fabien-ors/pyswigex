import os
import sys
import shutil
import glob
import subprocess
try:
    from setuptools import setup, Extension, Command
    from setuptools.command.build_py import build_py as build_py
    from setuptools.command.build_ext import build_ext as build_ext
except:
    from distutils import setup, Extension, Command
    from distutils.command.build_py import build_py as build_py  
    from distutils.command.build_ext import build_ext as build_ext
    
# Module name (must be the same than the one in .i file)
module_name = "fibo"

# Add C++ body source files and the unique SWIG interface file in extensions list (see build_ext command)
cpps = glob.glob(os.path.join('src','*.cpp'))
module_int = os.path.join('src', module_name + '.i')
module_ext = Extension('_' + module_name,
                       sources = cpps + [module_int], # Keep SWIG interface file in last position
                       swig_opts = ['-c++'], # https://lists.debian.org/debian-user/2008/03/msg01744.html
                      )

class Doxygen(Command):
    description = "Regenerate HTML and XML documentation from C++ code (requires doxygen)"
    user_options = []
    
    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        os.chdir('doxygen')
        try:
            cmd = ['doxygen', 'Doxyfile']
            print("Running command: ", cmd)
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as cpe:
            pass
        finally:
            os.chdir(self.cwd)

class Doxy2Swig(Command):
    description = "Regenerate SWIG docstring documentation from XML doxygen documentation"
    user_options = []
    
    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        if (not os.path.isfile('doxygen/xml/index.xml')):
            print("Launch doxygen command before doxy2swig")
        else:
            os.chdir('doxygen')
            if (sys.platform.startswith("win")):
                pycmd = "python"
            else: 
                pycmd = "python3"
            cmd = [pycmd, 'doxy2swig.py', 'xml/index.xml', '../src/documentation.i']
            print("Running command: ", cmd)
            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError as cpe:
                pass
            finally:
                os.chdir(self.cwd)

class MyBuildExt(build_ext):
    """ Override build_ext command so that some customized commands are executed:
        1- documentation generation (doxygen)
        2- documentation conversion to swig docstring (doxy2swig)
        3- Python wrapper interface generation (swig)
    """ 
    def run(self):
        self.run_command("doxygen")
        self.run_command("doxy2swig")
        return super().run() # Run swig thanks to extensions list above

# https://github.com/pypa/setuptools/issues/1347#issuecomment-387802255
class MyClean(Command):
    description = "Custom clean command to really remove all undesirable stuff"
    user_options = []
    
    to_be_cleaned = ['./dist',
                     './build',
                     './setup.cfg',
                     './src/*.egg-info',
                     './src/__pycache__',
                     './src/' + module_name + '.py',
                     './src/' + module_name + '_wrap.*',
                     './src/*.so',
                     './doxygen/html',
                     './doxygen/xml',
                     './src/documentation.i']
                   
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Get directory containing setup.py
        root_dir = os.path.abspath(os.path.dirname(__file__))

        # Parse all stuff to be cleaned and deleted
        for path_pattern in self.to_be_cleaned:
            # Make paths absolute
            abs_paths = glob.glob(os.path.join(root_dir, path_pattern))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(root_dir):
                    # Die if path in to_be_cleaned is outside root directory
                    raise ValueError("%s is not a path inside %s" % (path, root_dir))
                print('Removing %s' % os.path.relpath(path))
                if (os.path.isfile(path)):
                    os.remove(path)     # remove one file
                else:
                    shutil.rmtree(path) # rmtree does not know how to remove files
                
                
# https://stackoverflow.com/questions/29477298/setup-py-run-build-ext-before-anything-else
class MyBuildPy(build_py):
    """ Override build_py command so that build_ext command is executed before building the package.""" 
    def run(self):
        self.run_command("build_ext")
        return super().run() # Really run build_py

# Load readme file       
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyswigex",
    version="0.0.2",
    author="Fabien Ors",
    author_email="fabien.ors@mines-paristech.fr",
    description="Ready-to-use complete example of a cross-platform Python source package built from C++ library using SWIG and doxygen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fabien-ors/pyswigex",
    project_urls={
        "Bug Tracker": "https://github.com/fabien-ors/pyswigex/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    ext_modules=[module_ext],
    py_modules=[module_name],
    cmdclass={
        'build_py'  : MyBuildPy,
        'build_ext' : MyBuildExt,
        'doxygen'   : Doxygen,
        'doxy2swig' : Doxy2Swig,
        'clean'     : MyClean,
    },
    package_dir={"": "src"},
    python_requires=">=3",
)

fh.close()
