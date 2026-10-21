def count_votes(ballots):
    counts = {}
    for ballot in ballots:
        choice = ballot["choice"]
        counts[choice] += 1
    return counts


def we_are_not_friends(person):
    return person["friends"].pop(0)


def change_email(account, email):
    updated = account
    updated["email"] = email
    return updated
