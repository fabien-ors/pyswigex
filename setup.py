import subprocess
import setuptools

# Thanks to https://pypi.org/project/swigibpy/
from os import chdir, getcwd
from os.path import join, dirname, abspath

try:
    from setuptools.command.build_ext import build_ext
    from setuptools import setup, Extension, Command
except:
    from distutils.command.build_ext import build_ext
    from distutils import setup, Extension, Command

module_name = "fibo"
module_wrap = module_name + '_wrap.cpp'
module_header = module_name + '.hpp'
module_interface = module_name + '.i'
root_dir = abspath(dirname(__file__))
package_dir = join(root_dir, "src")

module_ext = Extension('_' + module_name,
                       sources=[join(package_dir, module_wrap)],
                      )

def swigify():
    cwd = getcwd()
    swig_opts = [
      '-v',
      '-c++',
      '-python',
      '-outdir', package_dir
      ]

    chdir(package_dir)
    try:
        swig_cmd = ['swig'] + swig_opts + ['-o', module_wrap]
        swig_cmd.append(join(package_dir, module_interface))
        subprocess.check_call(swig_cmd)
    except subprocess.CalledProcessError as cpe:
        pass
    finally:
        chdir(cwd)

class Swigify(Command):
    description = "Regenerate module's wrapper code (requires SWIG)"
    user_options = []

    def run(self):
        swigify()



class FiboBuildExt(build_ext):
              
    def run(self):
        # Generate Swig wrapper
        print("Launching SWIG...")
        swigify()
        
        # Build all
        print("Building Package...")
        build_ext.run(self)

    def build_extensions(self):
        try:
            cmd = ['python3'] + ['-m', 'pybind11'] + ['--includes']
            # https://stackoverflow.com/questions/2502833/store-output-of-subprocess-popen-call-in-a-string
            flags = subprocess.check_output(cmd).decode("utf-8")
            print(flags)            
        except subprocess.CalledProcessError as cpe:
            pass
            
        # Customize flags for gcc (keep the trailing coma)
        extra = (flags + ' -D_USE_PYBIND',)
        for ext in self.extensions:
            ext.extra_compile_args += extra
        build_ext.build_extensions(self)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-fabien-ors",
    version="0.1.0",
    author="Fabien Ors",
    author_email="fabien.ors@mines-paristech.fr",
    description="A small example package from official tutorial using SWIG",
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
      'build_ext': FiboBuildExt,
    },
    package_dir={"": "src"},
    python_requires=">=3.6",
)

fh.close()
