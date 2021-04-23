import unittest

from User_Registration import UserRegistration


class TestUserRegistration(unittest.TestCase):

    def test_first_name_regex_givenCorrectName_shouldReturnTrue(self):
        first_name = "Amit"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        self.assertTrue(result)

    def test_first_name_regex_giveIncorrectName_shouldReturnFalse(self):
        first_name = "amit"
        user = UserRegistration()
        result = user.first_name_regex(first_name)
        self.assertFalse(result)

    def test_last_name_regex_givenCorrectName_shouldReturnTrue(self):
        last_name = "Kumar"
        user = UserRegistration()
        result = user.last_name_regex(last_name)
        self.assertTrue(result)

    def test_last_name_regex_givenIncorrectName_shouldReturnFalse(self):
        last_name = "kumar"
        user = UserRegistration()
        result = user.last_name_regex(last_name)
        self.assertFalse(result)

    def test_email_regex_givenCorrectEmail_shouldReturnTrue(self):
        email = "ak657harley@gmail.com"
        user = UserRegistration()
        result = user.email_regex(email)
        self.assertTrue(result)

    def test_email_regex_givenIncorrectEmail_shouldReturnFalse(self):
        email = "abc.100@hggdb.cvjhdb"
        user = UserRegistration()
        result = user.email_regex(email)
        self.assertFalse(result)

    def test_phone_number_regex_givenCorrectPhoneNumber_shouldReturnTrue(self):
        phone_number = "91 8210029078"
        user = UserRegistration()
        result = user.phone_number_regex(phone_number)
        self.assertTrue(result)

    def test_phone_number_regex_givenIncorrectPhoneNumber_shouldReturnTrue(self):
        phone_number = "918210029078"
        user = UserRegistration()
        result = user.phone_number_regex(phone_number)
        self.assertFalse(result)

    def test_password_regex_givenCorrectPassword_shouldReturnTrue(self):
        password = "doD12#nbD"
        user = UserRegistration()
        result = user.password_regex(password)
        self.assertTrue(result)

    def test_password_regex_givenIncorrectPassword_shouldReturnTrue(self):
        password = "source"
        user = UserRegistration()
        result = user.password_regex(password)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
