# Python Code Style

A GitHub action that helps python code to adhere
to our style guide for python code at celebrate company.

## Linters

- flake8
- mypy
- pylint

## Usage

This action ONLY runs the linters.
The python environment should be set up separately.

```yaml
name: celebrate python linting
uses: kartenmacherei/python-code-style@0.0.1
```

## Features

- Runs python linters one after the other; fails with the first failing linter
- If triggered by a pull request, linter results will be added as comments to the PR.
