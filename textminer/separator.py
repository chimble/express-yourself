import re


def words(input):
    try:
        new_list = re.findall(r'^[a-zA-Z0-9\-\s]+[a-zA-Z]$', input)
        new_list = new_list[0]
        return new_list.split(' ')
    except:
        return None


def phone_number(input):
    numbers = re.findall(r'([0-9])', input)
    if len(numbers) != 10:
        return None
    new_dict = {}
    new_dict['area_code'] = ''.join(numbers[0:3])
    first_part = ''.join(numbers[3:6])
    second_part = ''.join(numbers[6:10])
    new_dict['number'] = first_part + '-' + second_part
    return(new_dict)


def money(input):
    if re.findall(r'^\$([0-9]+(,[0-9]{3})*)(\.[0-9]{2})?$', input):
        numbers = re.findall(r'([0-9])', input)
        symbol = re.findall(r'\$', input)
        cents = re.findall(r'\.[0-9]{2}$', input)
        if cents:
            numbers = numbers[:-2]
        new_dict = {}
        new_dict['currency'] = ''.join(symbol[0])
        if cents:
            new_dict['amount'] = float(''.join(numbers)+cents[0])
        else:
            new_dict['amount'] = float(''.join(numbers))
        print(new_dict)
        return(new_dict)
    else:
        return None


def zipcode(input):
    zip_num = re.findall(r'([0-9])', input)
    if len(zip_num) == 5:
        new_dict = {}
        new_dict['zip'] = ''.join(zip_num)
        new_dict['plus4'] = None
        print(new_dict)
        return new_dict
    elif len(zip_num) == 9:
        new_dict = {}
        new_dict['zip'] = ''.join(zip_num[0:5])
        new_dict['plus4'] = ''.join(zip_num[5:9])
        print(new_dict)
        return new_dict


def date(input):
    if re.findall(r'^[0-9]+/[0-9]+/[0-9]{4}', input):
        month = re.findall(r'^[0-9]+/', input)
        day = re.findall(r'/[0-9]+/', input)
        year = re.findall(r'/[0-9]+$', input)
        new_dict = {}
        new_dict['month'] = int(month[0][:-1])
        new_dict['day'] = int(day[0][1:-1])
        new_dict['year'] = int(year[0][1:])
        print(new_dict)
        return new_dict
    elif re.findall(r'^[0-9]+-[0-9]+-[0-9]+', input):
        year = re.findall(r'^[0-9]{4}', input)
        day = re.findall(r'-[0-9]+$', input)
        month = re.findall(r'-[0-9]+-', input)
        new_dict = {}
        new_dict['day'] = int(day[0][1:])
        new_dict['month'] = int(month[0][1:-1])
        new_dict['year'] = int(year[0])
        return(new_dict)

    else:
        return None
