# Example of a python package distributed under TestPyPi

TestPyPi URL :
https://test.pypi.org/project/example-pkg-fabien-ors/


## References:

Package example following this tutorial :
https://packaging.python.org/tutorials/packaging-projects

Modified in order to use SWIG (c++ to python) inspired by :
https://pypi.org/project/swigibpy


## Installation:

### From TestPyPi:

Installation:
```sh
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-fabien-ors
```
Upgrade:
```sh
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-fabien-ors --upgrade
```

### From local directory:
Installation:
```sh
python3 -m pip install -e .
```
Note: Command to be executed from `packaging_tutorial` directory (see below)


## Usage:

```python
import fibo
fibo.fib(10)
help(fibo.fib)
```

## Reminder:

Stuff coming from https://packaging.python.org/tutorials/packaging-projects/

### Create package tree:

Create folders and add your c++ code in the `src` :
```
packaging_tutorial/
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
All the following commands are executed from the packaging_tutorial directory.

### Github repository creation:
```sh
git init
git add *
git commit
git remote add origin https://github.com/fabien-ors/example-pkg
git push -u origin master
```

### Update your code:
Modify or add python modules or c++ source code in `src` folder, then update your git repository:
```sh
git add *
git commit
git push
```
Note: You can test your package by installing it locally before building and uploading it to TestPyPi (see above).

### Clean package:
```sh
# Remove setuptools stuff:
rm -rf dist build
rm -rf src/*.egg-info
rm -rf src/__pycache__
# Remove swig stuff:
rm -rf src/*.py
rm -rf src/*_wrap.*
rm -rf src/*.so
```

### Build package:
```sh
python3 -m build
```

### Upload to TestPyPi:
Each time you want to upload, you MUST upgrade the version in `setup.py` file!
https://stackoverflow.com/questions/56520660/upload-a-new-release-to-testpypi

```sh
python3 -m twine upload --repository testpypi dist/*
```

### Remove installed package:
```sh
python3 -m pip uninstall example-pkg-fabien-ors
```

***

## License

MIT

2021 Fabien Ors
