def get_first_item(items):
    return items[0]


def we_are_not_friends(person):
    return person["friends"].pop(0)


def add_hobby(person, hobby):
    updated = person
    updated["hobbies"].append(hobby)
    return updated
