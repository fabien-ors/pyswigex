import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-fabien-ors",
    version="0.0.5",
    author="Fabien Ors",
    author_email="fabien.ors@mines-paristech.fr",
    description="A small example package from official tutorial",
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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

