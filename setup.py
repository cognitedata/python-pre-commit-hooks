from setuptools import find_packages, setup

setup(
    name="cognite_pre_commit_hooks",
    description="Cognite pre-commit hooks",
    url="https://github.com/cognitedata/python-pre-commit-hooks",
    version="1.0.0",
    author="Erlend Vollset",
    author_email="erlend.vollset@cognite.com",
    packages=find_packages(exclude=("tests*", "testing*")),
    install_requires=["black", "isort"],
)
