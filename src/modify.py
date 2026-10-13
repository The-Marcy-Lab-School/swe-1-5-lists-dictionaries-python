def clear_list(items):
    items.clear()
    return items


def have_birthday(person):
    age = person["age"]
    age = age + 1


def count_by_owner(pets):
    counts = {}
    for owner in pets.keys():
        counts[owner] = len(pets[owner])
    return counts
