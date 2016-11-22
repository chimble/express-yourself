import re


def phone_numbers(input):
    return re.findall(r'\(*[0-9]{3}.*[0-9]{3}.*[0-9]{4}', input)
