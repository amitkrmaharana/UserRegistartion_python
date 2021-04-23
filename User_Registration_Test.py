import unittest

from User_Registration import UserRegistration


class TestUserRegistration(unittest.TestCase):

    def test_first_name_regex_givenCorrectName_shouldReturnTrue(self):
        first_name = "Amit"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        self.assertTrue(result)

    def test_first_name_regex_givenCorrectName_shouldReturnFalse(self):
        first_name = "amit"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        self.assertFalse(result)

    def test_last_name_regex_givenCorrectName_shouldReturnTrue(self):
        last_name = "Kumar"
        user = UserRegistration()
        result = user.last_name_regex(last_name)
        self.assertTrue(result)

    def test_last_name_regex_givenCorrectName_shouldReturnFalse(self):
        last_name = "kumar"
        user = UserRegistration()
        result = user.last_name_regex(last_name)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
