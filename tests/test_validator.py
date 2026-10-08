import unittest

from password_validator import is_password_secure, validate_password


class TestValidPasswords(unittest.TestCase):
    def test_original_example_is_secure(self):
        self.assertTrue(is_password_secure("Gh$#4ghg"))

    def test_long_password_is_secure(self):
        self.assertTrue(is_password_secure("Correct-Horse9Battery"))

    def test_exactly_minimum_length_is_secure(self):
        self.assertTrue(is_password_secure("aB3$efgh"))


class TestLength(unittest.TestCase):
    def test_too_short(self):
        self.assertFalse(is_password_secure("aB3$efg"))

    def test_empty_string(self):
        self.assertFalse(is_password_secure(""))

    def test_custom_min_length(self):
        self.assertFalse(is_password_secure("aB3$efghij", min_length=12))
        self.assertTrue(is_password_secure("aB3$efghijkl", min_length=12))


class TestCharacterRules(unittest.TestCase):
    def test_missing_uppercase(self):
        self.assertFalse(is_password_secure("gh$#4ghg"))

    def test_missing_lowercase(self):
        self.assertFalse(is_password_secure("GH$#4GHG"))

    def test_missing_digit(self):
        self.assertFalse(is_password_secure("Gh$#aghg"))

    def test_missing_special(self):
        self.assertFalse(is_password_secure("Gh4Xaghg"))

    def test_space_rejected(self):
        self.assertFalse(is_password_secure("Gh$# 4ghg"))

    def test_triple_repeat_rejected(self):
        self.assertFalse(is_password_secure("Gh$#4aaag"))

    def test_double_repeat_allowed(self):
        self.assertTrue(is_password_secure("Gh$#4aagx"))


class TestCommonPasswords(unittest.TestCase):
    def test_common_password_rejected(self):
        result = validate_password("P@ssw0rd")
        self.assertFalse(result.is_valid)
        self.assertIn("Is too common", result.errors)


class TestValidationResult(unittest.TestCase):
    def test_valid_has_no_errors(self):
        result = validate_password("Gh$#4ghg")
        self.assertTrue(result.is_valid)
        self.assertEqual(result.errors, ())

    def test_reports_every_failure(self):
        result = validate_password("abc")
        self.assertEqual(len(result.errors), 4)

    def test_non_string_raises(self):
        with self.assertRaises(TypeError):
            validate_password(12345678)


if __name__ == "__main__":
    unittest.main()
