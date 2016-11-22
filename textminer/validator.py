import re


def binary(string_num):
    return re.search(r'^[0-1]+$', string_num)


def binary_even(string_num):
    return re.search(r'^[0-1]+0$', string_num)


def hex(string_hex):
    return re.search(r'^[a-fA-F0-9]+$', string_hex)


def word(string_word):
    return re.search(r'^[a-zA-Z0-9\-]+[a-zA-Z]$', string_word)


def words(string_words, **kwargs):
    words_count = len(string_words.split(' '))
    if kwargs:
        if kwargs['count'] == words_count:
            return re.search(r'^[a-zA-Z0-9\-\s]+[a-zA-Z]$', string_words)
        else:
            return None
    else:
        return re.search(r'^[a-zA-Z0-9\-\s]+[a-zA-Z]$', string_words)


def phone_number(string_phone):
    return re.search(r'\(*[0-9]{3}.*[0-9]{3}.*[0-9]{4}', string_phone)


def money(string_money):
    return re.search(r'^\$[0-9]+\.[0-9]{2}$|^\$[0-9]+$|^\$[0-9]+,[0-9]{3},*[0-9]*$|^\$[0-9]+,[0-9]{3},*[0-9]*\.[0-9]{2}$', string_money)


def zipcode(string_zip):
    return re.search(r'^[0-9]{5}$|^[0-9]{5}\-[0-9]{4}$', string_zip)


def date(string_date):
    return re.search(r'^[0-9]*/[0-9]*/[0-9]*$|^[0-9]*\-[0-9]*\-[0-9]*$', string_date)
