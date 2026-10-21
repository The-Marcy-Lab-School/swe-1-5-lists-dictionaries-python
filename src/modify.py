def add_guest(guests, name):
    guests.append(name)
    return guests


def get_passing_students(grades, passing_score):
    passing = []
    for name in grades:
        if grades[name] >= passing_score:
            passing.append(name)
    return passing
