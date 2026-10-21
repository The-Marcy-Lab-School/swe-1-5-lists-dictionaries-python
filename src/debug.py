def get_first_item(items):
    return items[0]


def we_are_not_friends(person):
    return person["friends"].pop(0)


def change_email(account, email):
    updated = account
    updated["email"] = email
    return updated
