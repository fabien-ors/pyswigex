# Example of a python package distributed under TestPyPi

Package example following this tutorial :
https://packaging.python.org/tutorials/packaging-projects/


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
import example_pkg
example_pkg.fib(10)
help(example_pkg.fib)
```
Note: The fib function is directly available since `fibo.py` is imported in `__init__.py`


## Reminder:

Stuff coming from https://packaging.python.org/tutorials/packaging-projects/

### Create package tree:

Create folders and add your python code in the `src/example_pkg` folder:
```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.py
├── src/
│   └── example_pkg/
│       ├── __init__.py
│       ├── fibo.py
│       └── yourcode.py
└── tests/
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
Modify or add python modules in `src/example_pkg` folder, then update your git repository:
```sh
git add *
git commit
git push
```
Note: You can test your package by installing it locally before building and uploading it to TestPyPi (see above).

### Clean package:
```sh
rm -rf dist build
rm -rf src/*.egg-info
rm -rf src/*/__pycache__
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
