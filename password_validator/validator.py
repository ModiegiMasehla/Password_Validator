import re
import string
from dataclasses import dataclass

MIN_LENGTH = 8
SPECIAL_CHARACTERS = string.punctuation

COMMON_PASSWORDS = frozenset({
    "password", "password1", "password123", "12345678", "123456789",
    "qwerty123", "qwertyuiop", "letmein123", "welcome1", "admin123",
    "iloveyou", "abc12345", "p@ssw0rd", "p@ssword1", "passw0rd",
})


@dataclass(frozen=True)
class ValidationResult:
    errors: tuple = ()

    @property
    def is_valid(self):
        return not self.errors


def validate_password(password, min_length=MIN_LENGTH):
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    errors = []

    if len(password) < min_length:
        errors.append(f"Must be at least {min_length} characters long")
    if not any(c.isupper() for c in password):
        errors.append("Must contain an uppercase letter")
    if not any(c.islower() for c in password):
        errors.append("Must contain a lowercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("Must contain a digit")
    if not any(c in SPECIAL_CHARACTERS for c in password):
        errors.append("Must contain a special character")
    if any(c.isspace() for c in password):
        errors.append("Must not contain spaces")
    if re.search(r"(.)\1\1", password):
        errors.append("Must not repeat the same character 3 times in a row")
    if password.lower() in COMMON_PASSWORDS:
        errors.append("Is too common")

    return ValidationResult(tuple(errors))


def is_password_secure(password, min_length=MIN_LENGTH):
    return validate_password(password, min_length).is_valid
