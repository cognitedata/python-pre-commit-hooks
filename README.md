<a href="https://cognite.com/">
    <img src="https://github.com/cognitedata/cognite-sdk-python/blob/master/cognite_logo.png" alt="Cognite logo" title="Cognite" align="right" height="80" />
</a>

Pre-commit hooks for Python
==========================
This repository contains pre-commit hook definitions to be used with the [pre-commit](https://github.com/pre-commit/pre-commit) library.

## Hooks
- [iSort](https://github.com/timothycrosley/isort)
- [black](https://github.com/ambv/black)

## Usage
These pre-commit hooks are configured to be used in a pipenv project.
In order to use these pre-commit hooks in your project follow these steps

### Install the pre-commit library in your project by running this command
```python
$ pipenv install pre-commit
```
### Add a .pre-commit-config.yaml file to your project root with the following content
```yaml
repos:
- repo: https://github.com/cognitedata/python-pre-commit-hooks
  rev: <latest-commit-ref>
  hooks:
  - id: isort
  - id: black
```
### Install the pre-commit hooks by running this command
```python
$ pre-commit install
```
