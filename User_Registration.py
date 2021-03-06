import re


class UserRegistration:

    def __init__(self):
        pass

    def first_name_regex(self, first_name):
        name_pattern = r"^[A-Z]{1}[a-zA-Z]{2,}$"
        return bool(re.match(name_pattern, first_name))

    def last_name_regex(self, last_name):
        name_pattern = r"^[A-Z]{1}[a-zA-Z]{2,}$"
        return bool(re.match(name_pattern, last_name))

    def email_regex(self, email):
        email_pattern = "^[a-zA-Z0-9]{3,}([\\.\\+\\-]?[a-zA-Z0-9]{3,})?[@][A-Za-z0-9]{1,}[.][A-Za-z]{2,4}[,]?([.][A-Za-z]{2,4}[.]?)?$"
        return bool(re.match(email_pattern, email))

    def phone_number_regex(self, phone_number):
        phone_number_pattern = "^[9][1][ ][6-9][0-9]{9}$"
        return bool(re.match(phone_number_pattern, phone_number))

    def password_regex(self, password):
        password_regex = "^(?=.*[\\@\\#\\$\\%\\&\\_\\,\\.])(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{8,}$"
        return bool(re.match(password_regex, password))
