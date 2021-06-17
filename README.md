## Overview
The idea of this **minimal example** package is to show how to distribute a C++ library as a **cross-platform** python source package under PyPi site index and using SWIG. Currently, this package only provides two fibonacci functions but feel free to add your own C++ code starting from this example.

  * TestPyPi download URL: https://test.pypi.org/project/example-pkg-fabien-ors
  * GitHub source: https://github.com/fabien-ors/example-pkg

## References
This package example follows [this tutorial](https://packaging.python.org/tutorials/packaging-projects).
It has been modified in order to use SWIG (c++ to python) according [this documentation](https://docs.python.org/3/distutils/setupscript.html).
Some tricks and advices come from [this package](https://pypi.org/project/swigibpy/)

## Requirements
For using this package, the following tools must be available:
  * Python 3 or higher with pip module installed
  * SWIG 4 or higher
  * GCC compiler 5.4 or higher (Linux/MacOs) or Microsoft Visual C++ Compiler 14 or higher (Windows)
  * Git client (only if your are installing from source)
  
### Linux required tools installation:
Under Linux, the GCC compiler is already installed
```sh
sudo apt install python3-pip
sudo apt install swig
sudo apt install git
```
### MacOS required tools installation:
Under MacOS, the GCC (or Clang) compiler is already installed (Not yet tested)
```sh
brew install swig
brew install python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
sudo apt install git
```
### Windows required tools installation:
Download and install the following tools:
  * Python 3+ [from here](https://www.python.org/downloads) (which comes with pip)
  * SWIG 4+ [from here](http://www.swig.org/download.html) (extract the archive in a directory of yours, let's say *C:\swigwin-4.0.2*, see Notes below)
  * Microsoft Visual C++ Compiler 14+ [from here](https://visualstudio.microsoft.com/visual-cpp-build-tools) (see Notes below)
  * Git client [from here](https://gitforwindows.org)
  
Notes:
  * The full Visual Studio C++ IDE is not necessary. You can 'only' download Visual Studio Build Tools (1,4Go!) (more details [here](https://stackoverflow.com/a/44398715))
  * The *Path* environment variable must be updated to make *swig.exe* available in the batch command line (follow [this guide](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho) to add *C:\swigwin-4.0.2* folder in the *Path* variable and restart Windows)
  * The Windows C++ Compiler used by `pip install` must be the same that the one used for compiling Python (Visual C++). If you prefer using another smaller compiler (i.e. MinGW), you could [try this](https://wiki.python.org/moin/WindowsCompilers#GCC_-_MinGW-w64_.28x86.2C_x64.29) (not tested)
  

## Installation from TestPyPi
Note for Windows user: 
  * In all commands below, use `python.exe` (in place of `python3`) and `git.exe` (in place of `git`)

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

## Install from sources
Cloning the repository and installing
```sh
git clone https://github.com/fabien-ors/example-pkg
cd example-pkg
python3 -m pip install -e .
```
Or directly installing from github
```sh
python3 -m pip install -U git+https://github.com/fabien-ors/example-pkg.git
```

## Usage
You can look at *tests* directory or execute following python commands:
```python
import fibo
fibo.fib(50)
help(fibo.fib)
```

## Development
Some of the next commands are git recalls.<br/>
Others are used for developping and building new versions of this package.<br/>
They must be executed from *example-pkg* directory.

### Create a package tree
Create initial structure of the package tree and add your c++ code in the *src* folder:
```
example-pkg/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.py
├── src/
│   ├── fibo.i
│   ├── fibo.hpp
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
  * You can test your package by installing it locally before building and uploading it to TestPyPi (see *Install from sources* above)

### Clean
This command remove setuptools and SWIG generated stuffs:
```sh
rm -rf dist build setup.cfg src/*.egg-info src/__pycache__ src/*.py src/*_wrap.* src/*.so
```

Because the clean option of setuptools does not remove a lot: 
```sh
python3 setup.py clean --all
```

### Build before uploading
Only build the source archive (tar.gz) (no prebuild version generated as it is OS specific):
```sh
python3 setup.py sdist
```

### Upload to TestPyPi
Each time you want to upload, you MUST upgrade the version in *setup.py* file! (see [this thread](https://stackoverflow.com/questions/56520660/upload-a-new-release-to-testpypi))
```sh
python3 -m twine upload --repository testpypi dist/*.tar.gz
```

### Remove installed package
Not really necessary but just to be confident:
```sh
python3 -m pip uninstall example-pkg-fabien-ors
```

You may sometimes need to remove the site-packages reference to the old version (see [this thread](https://stackoverflow.com/questions/43177200/assertionerror-egg-link-does-not-match-installed-location-of-reviewboard-at))
```sh
rm <path_to_site_package>/example-pkg-fabien-ors.egg-link
```

***

## License

MIT

2021 Fabien Ors
