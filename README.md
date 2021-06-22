## Overview
The idea of this **ready to use example** package is to show how to:
  * Build a **cross-platform** python **source package** based on a **C++ library** using **SWIG**
  * Generate **doxygen** documentation and make it available to Python users using **doxy2swig**
  * Distribute the Python package under **PyPi** site index
  
Currently, this package only provides a class which handles fibonacci series, but feel free to **adapt this example** adding your own C++ code.
  * TestPyPi download URL: https://test.pypi.org/project/example-pkg-fabien-ors
  * GitHub source: https://github.com/fabien-ors/example-pkg
  
## References
This package example follows [this tutorial](https://packaging.python.org/tutorials/packaging-projects).
It has been modified in order to use SWIG (c++ to python) according [this documentation](https://docs.python.org/3/distutils/setupscript.html).
Some tricks and advices come from [this package](https://pypi.org/project/swigibpy/).

This package contains a copy of [doxy2swig](https://github.com/m7thon/doxy2swig) python script (see LICENSE in *doxygen* folder)

## Requirements
For using this package, the following tools must be available (See required tools installation instructions below):
  * [Python](https://www.python.org/downloads) 3 or higher with pip module installed
  * [SWIG](http://www.swig.org/download.html) 4 or higher
  * [Doxygen](https://www.doxygen.nl/download.html) 1.8.3 or higher
  * [GCC](https://gcc.gnu.org) compiler 5.4 or higher (Linux/MacOS) or [Microsoft Visual C++ Compiler](https://visualstudio.microsoft.com/visual-cpp-build-tools) 14 or higher (Windows)
  * [Git](https://git-scm.com/downloads) client (only if your are installing from source)

## Package installation from TestPyPi
Installation:
```sh
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --no-cache-dir example-pkg-fabien-ors
```
Upgrade:
```sh
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --no-cache-dir example-pkg-fabien-ors --upgrade
```
Notes:
  * **--index-url** is used because by default, pip looks for packages into PyPi (not TestPyPi)
  * **--extra-index-url** is used because there is some limitations: test.pypi.org cannot use setuptools! (see [this thread](https://github.com/ultrajson/ultrajson/issues/366))
  * **--no-cache-dir** is used to ensure downloading last version from TestPyPi (see [this thread](https://stackoverflow.com/questions/9510474/removing-pips-cache))
  
## Package installation from sources
Cloning the repository and installing
```sh
git clone https://github.com/fabien-ors/example-pkg
cd example-pkg
python3 -m pip install .
```
Or directly installing from github
```sh
python3 -m pip install -U git+https://github.com/fabien-ors/example-pkg.git
```

## Usage
You can look at *tests* directory or execute following python commands:
```python
import fibo
f = fibo.Fibo(250)
help(fibo.Fibo.display)
f.display()
v = f.get()
print("v=",v)
```

## Required tools installation
This package has been successfully tested with Ubuntu 18.04 LTS and Windows 10

### Linux (Ubuntu):
Under Linux, the GCC compiler is already installed
```sh
sudo apt install python3-pip
sudo apt install swig
sudo apt install doxygen
sudo apt install git
```

### MacOS:
Under MacOS, the GCC (or Clang) compiler is already installed (Not tested)
```sh
brew install python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
brew install swig
brew install doxygen
brew install git
```

### Windows:
Download and install the following tools:
  * Python 3+ [from here](https://www.python.org/downloads) (which comes with pip and which is installed in *C:\\Python39* for example)
  * SWIG 4+ [from here](http://www.swig.org/download.html) (extract the archive in a directory of yours, let's say *C:\\swigwin-4.0.2*, see Notes below)
  * Doxygen 1.8.3+ [from here](https://www.doxygen.nl/download.html) (installed in the directory *C:\\doxygen* for example)
  * Microsoft Visual C++ Compiler 14+ [from here](https://visualstudio.microsoft.com/visual-cpp-build-tools) (see Notes below)
  * Git client [from here](https://gitforwindows.org)
  
Notes:
  * The full Visual Studio C++ IDE is not necessary. You can 'only' download Visual Studio Build Tools (1,4Go!) (more details [here](https://stackoverflow.com/a/44398715))
  * The *Path* environment variable must be updated to make *python.exe*, *swig.exe* and *doxygen.exe* available in the batch command line (follow [this guide](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho) to add *C:\\Python39*, *C:\\swigwin-4.0.2* and *C:\\doxygen\\bin* folder in the *Path* variable and restart Windows)
  * The Windows C++ Compiler used by `pip install` must be the same that the one used for compiling Python (Visual C++). If you prefer using another smaller compiler (i.e. MinGW), you could [try this](https://wiki.python.org/moin/WindowsCompilers#GCC_-_MinGW-w64_.28x86.2C_x64.29) (not tested)
  * In all commands below, Windows users must use `python.exe` (in place of `python3`) and `git.exe` (in place of `git`)

## Development
Some of the next commands are git recalls. Others are used for developping and building new versions of this package. They must be executed from *example-pkg* directory. If you want to give a relevant name to your python module, you must find the pattern *fibo* in all files and replace it by your own module name. To change the package name, you must update the first argument of the `setup` command (*example-pkg-fabien-ors*) in th *setup.py* file.

### Create a package tree
Create initial structure of your own package and add your c++ code in the *src* folder. Mandatory files are *pyproject.toml*, *LICENSE*, *README.md* and *setup.py*. Here is the folders tree of this package:
```
example-pkg/
├── LICENSE
├── pyproject.toml
├── MANIFEST.in
├── README.md
├── setup.py
├── doxygen/
│   ├── Doxyfile
│   ├── doxy2swig.py
│   └── LICENSE
├── src/
│   ├── fibo.i
│   ├── fibo.hpp
│   ├── fibo.cpp
│   └── yourcode.[cpp/hpp]
└── tests/
    └── test_fibo.py
```

### Create a git repository
This is done only once when creating a new package:
```sh
git init
git add *
git commit
git remote add origin https://github.com/fabien-ors/example-pkg
git push -u origin master
```

### Update the code
Modify or add c++ source code in *src* folder, update *fibo.i* accordingly and then, update your git repository:
```sh
git add *
git commit
git push
```
Notes:
  * You may have to git add *.gitignore* which is not selected by `git add *`
  * You can test your package by installing it locally before building and uploading it to TestPyPi (see *Install from sources in editable mode* below)

## Install from sources in editable mode
```sh
python3 -m pip install -e .
```

### Clean before building
Because the `clean --all` command of setuptools does not remove a lot, it has been overriden. Always execute this command before building and uploading the source package
```sh
python3 setup.py clean
```

### Build before uploading
Only build the source archive (tar.gz) (no prebuild version generated as it is OS specific):
```sh
python3 setup.py sdist
```

### Upload to TestPyPi
Each time you want to upload, you MUST upgrade the version in *setup.py* file! (see [this topic](https://stackoverflow.com/questions/56520660/upload-a-new-release-to-testpypi))
```sh
python3 -m twine upload --repository testpypi dist/*.tar.gz
```

### Remove installed package
Not really necessary but just to be confident:
```sh
python3 -m pip uninstall example-pkg-fabien-ors
```
You may sometimes need to remove the site-packages reference to the old version (see [this topic](https://stackoverflow.com/questions/43177200/assertionerror-egg-link-does-not-match-installed-location-of-reviewboard-at))
```sh
rm <path_to_site_package>/example-pkg-fabien-ors.egg-link
```

***

## License
MIT
2021 Fabien Ors
