from os.path import join
try:
    from setuptools import setup, Extension
    from setuptools.command.build_py import build_py as _build_py  
except:
    from distutils import setup, Extension
    from distutils.command.build_py import build_py as _build_py  

# Thanks to https://docs.python.org/3/distutils/setupscript.html
module_name = "fibo"

# Only add the SWIG interface file in extensions list
module_ext = Extension('_' + module_name,
                       sources=[
                           join('src', module_name + '.i')
                       ],
                       swig_opts=['-c++'], # https://lists.debian.org/debian-user/2008/03/msg01744.html
                      )

# Run build_ext (SWIG) prior to build_py
# https://stackoverflow.com/questions/29477298/setup-py-run-build-ext-before-anything-else
class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()

# Load reamdme file       
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="example-pkg-fabien-ors",
    version="0.1.9",
    author="Fabien Ors",
    author_email="fabien.ors@mines-paristech.fr",
    description="Minimal Example of a python source package using SWIG and distributed under TestPyPi",
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
    cmdclass={'build_py' : build_py},
    package_dir={"": "src"},
    python_requires=">=3",
)

fh.close()
