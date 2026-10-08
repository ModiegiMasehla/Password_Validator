# Password Validator

A small Python library and command-line tool that checks whether a password is secure and tells you exactly what is wrong when it is not.

## Rules

A password is secure when it:

- is at least 8 characters long (configurable)
- contains an uppercase letter, a lowercase letter, a digit and a special character
- contains no spaces
- does not repeat the same character 3 times in a row
- is not a commonly used password

## Requirements

Python 3.8 or newer. No third-party packages.

## Usage

As a library:

```python
from password_validator import is_password_secure, validate_password

is_password_secure("Gh$#4ghg")        # True

result = validate_password("abc")
result.is_valid                       # False
result.errors                         # tuple of messages explaining each failure
```

Custom minimum length:

```python
is_password_secure("aB3$efghijkl", min_length=12)
```

From the command line (input is hidden while you type):

```bash
python -m password_validator
```

Exit code is `0` for a secure password and `1` otherwise.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```
password-validator/
├── password_validator/
│   ├── __init__.py
│   ├── __main__.py
│   └── validator.py
├── tests/
│   └── test_validator.py
├── IMPROVEMENTS.txt
├── PUSH_STEPS.txt
├── pyproject.toml
└── README.md
```
