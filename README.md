# PythonTemplate

Python project template.

## Installation

Create a venv (optional but recommended):

```bash
python -m venv venv
# Linux
source venv/bin/activate
# Windows
venv/Scripts/Activate.ps1 on Windows
```

Install package:

```bash
# User installation
pip install .
# Developer editable installation
pip install -e .[dev]
```

## Run tests

```bash
pytest .
```

## Run formatter

```bash
ruff format .
```

## Run linter

```bash
ruff check .
mypy .
```
