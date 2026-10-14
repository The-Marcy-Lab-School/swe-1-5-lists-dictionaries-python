def get_first_item(items):
    return items[0]


def we_are_not_friends(person):
    return person["friends"].pop(0)


def add_hobby(person, hobby):
    updated = person
    updated["hobbies"].append(hobby)
    return updated


def set_first_item(items, value):
    items[0] = value
    return items


def set_first_letter(word, letter):
    word[0] = letter
    return word


def group_by_location(people):
    groups = {}
    for person in people:
        key = [person["city"], person["country"]]
        groups[key] = groups.get(key, 0) + 1
    return groups
