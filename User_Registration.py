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
