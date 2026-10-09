import sys
from getpass import getpass

from .validator import validate_password


def main():
    password = getpass("Enter a password to check: ")
    result = validate_password(password)

    if result.is_valid:
        print("Password is secure.")
        return 0

    print("Password is not secure:")
    for error in result.errors:
        print(f"  - {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
