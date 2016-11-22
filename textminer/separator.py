import re


def words(input):
    try:
        new_list = re.findall(r'^[a-zA-Z0-9\-\s]+[a-zA-Z]$', input)
        new_list = new_list[0]
        return new_list.split(' ')
    except:
        return None
    #return re.findall(r'^[a-zA-Z0-9\-\s]+[a-zA-Z]$', input)


def phone_number(input):
    #obb = re.match(r'^([0-9]{3})', input)
    bob = re.match(r'\(([0-9]{3})', input)
    bob1 = re.match(r'\(([0-9]{3})\).?([0-9]{3})', input)
    bob2 = re.match(r'\(([0-9]{3})\).?([0-9]{3}).?([0-9]{4})', input)

    print(bob.group(1))
    print(bob1.group(2))
    print(bob2.group(3))
    new_dict = {}
    new_dict['area_code']=bob.group(1)
    new_dict['number'] = str(bob1.group(2)) + '-' + str(bob2.group(3))
    print(new_dict)
    return new_dict
    # print(obb.group(1))
    # #print(obb.group(0))
    # print(obb.groups())
    #print(bob.group(2))
    # .?([0-9]{3}).?([0-9]{4})

#?P<area_code>
