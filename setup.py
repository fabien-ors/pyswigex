from os import chdir, getcwd
from os.path import join, isfile
from glob import glob
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
cpps = glob(join('src','*.cpp'))
module_ext = Extension('_' + module_name,
                       sources=[ join('src', module_name + '.i') ] + cpps,
                       swig_opts=['-c++'], # https://lists.debian.org/debian-user/2008/03/msg01744.html
                      )

class Doxygen(Command):
    description = "Regenerate HTML and XML documentation from C++ code (requires doxygen)"
    user_options = []
    
    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = getcwd()

    def run(self):
        chdir('doxygen')
        try:
            cmd = ['doxygen','Doxyfile']
            print("Running command: ", cmd)
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as cpe:
            pass
        finally:
            chdir(self.cwd)

class Doxy2Swig(Command):
    description = "Regenerate SWIG docstring documentation from XML doxygen documentation"
    user_options = []
    
    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = getcwd()

    def run(self):
        if (not isfile('doxygen/xml/index.xml')):
            print("Launch doxygen command before doxy2swig")
        else:
            chdir('doxygen')
            cmd = ['python3','doxy2swig.py','xml/index.xml','../src/documentation.i']
            print("Running command: ", cmd)
            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError as cpe:
                pass
            finally:
                chdir(self.cwd)

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

# https://stackoverflow.com/questions/29477298/setup-py-run-build-ext-before-anything-else
class MyBuildPy(build_py):
    """ Override build_py command so that build_ext command is executed before building the package
    """ 
    def run(self):
        self.run_command("build_ext")
        return super().run() # Really run build_py

# Load reamdme file       
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="example-pkg-fabien-ors",
    version="0.2.0",
    author="Fabien Ors",
    author_email="fabien.ors@mines-paristech.fr",
    description="Ready-to-use complete example of a python source package built from C++ library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fabien-ors/example-pkg",
    project_urls={
        "Bug Tracker": "https://github.com/fabien-ors/example-pkg/issues",
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
    },
    package_dir={"": "src"},
    python_requires=">=3",
)

fh.close()
