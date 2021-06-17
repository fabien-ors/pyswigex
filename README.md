## Overview
The idea of this **minimal example** package is to show how to distribute a C++ library as a python source package under PyPi site index and using SWIG.<br/>
Currently, this package only provides two fibonacci functions.<br/>
TestPyPi download URL: https://test.pypi.org/project/example-pkg-fabien-ors
GitHub source: https://github.com/fabien-ors/example-pkg

## References
This package example follows this tutorial: https://packaging.python.org/tutorials/packaging-projects

It has been modified in order to use SWIG (c++ to python) according: https://docs.python.org/3/distutils/setupscript.html

## Installation from TestPyPi
Installation:
```sh
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --no-cache-dir example-pkg-fabien-ors
```
Upgrade:
```sh
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --no-cache-dir example-pkg-fabien-ors --upgrade
```
Notes:
  * `--index-url` is used because by default, pip looks for packages into PyPi (not TestPyPi)
  * `--extra-index-url` is used because there is some limitations: test.pypi.org cannot use setuptools! (see https://github.com/ultrajson/ultrajson/issues/366)
  * `--no-cache-dir` is used to ensure downloading last version from TestPyPi (see https://stackoverflow.com/questions/9510474/removing-pips-cache)

## Install package from source
```sh
git clone https://github.com/fabien-ors/example-pkg
cd example-pkg
python3 -m pip install -e .
```

## Usage
You can look at `tests` directory or execute following python commands:
```python
import fibo
fibo.fib(50)
help(fibo.fib)
```

## Development
Some of the next commands are git recalls.<br/>
Others are used for developping and building new versions of this package.<br/>
They must be executed from `example-pkg` directory.

### Create a package tree
Create initial structure of the package tree and add your c++ code in the `src` folder:
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
Modify or add c++ source code in `src` folder, update `fibo.i` accordingly and then, update your git repository:
```sh
git add *
git commit
git push
```
Notes:
  * You may have to git add `.gitignore` which is not selected by `git add *`
  * You can test your package by installing it locally before building and uploading it to TestPyPi (see below)

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
Each time you want to upload, you MUST upgrade the version in `setup.py` file! (see https://stackoverflow.com/questions/56520660/upload-a-new-release-to-testpypi)
```sh
python3 -m twine upload --repository testpypi dist/*.tar.gz
```

### Remove installed package
Not really necessary but just to be confident:
```sh
python3 -m pip uninstall example-pkg-fabien-ors
```

You may sometimes need to remove the site-packages reference to the old version (see https://stackoverflow.com/questions/43177200/assertionerror-egg-link-does-not-match-installed-location-of-reviewboard-at)
```sh
rm <path_to_site_package>/example-pkg-fabien-ors.egg-link
```

***

## License

MIT

2021 Fabien Ors
