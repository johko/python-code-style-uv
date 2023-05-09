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

MAKE SURE TO PROVIDE YOUR OWN LINTER CONFIGURATION FILES IN YOUR REPOSITORY.

```yaml
name: celebrate python linting
uses: kartenmacherei/python-code-style@0.0.6
```

## Features

- Runs all specified python linters
- If triggered by a pull request, linter results will be added as comments to the PR.
- If triggered by a different kind of commit, linter results will be added as check errors.
