from debug import add_hobby, get_first_item, we_are_not_friends

TEST_SUITE_NAME = "Debug Tests"


def test_get_first_item():
    """get_first_item - returns the first item, or None when there is none"""
    assert get_first_item(["a", "b"]) == "a"
    assert get_first_item([1]) == 1
    assert get_first_item([]) is None


def test_we_are_not_friends():
    """we_are_not_friends - removes and returns the LAST friend"""
    person = {"name": "Sara", "friends": ["Bob", "Joe", "Sally"]}
    assert we_are_not_friends(person) == "Sally"
    assert person["friends"] == ["Bob", "Joe"]

    assert we_are_not_friends({"name": "Lonely", "friends": []}) is None


def test_add_hobby_is_pure():
    """add_hobby - returns a new person and leaves the original alone"""
    person = {"name": "Sara", "hobbies": ["hiking"]}
    updated = add_hobby(person, "biking")

    assert updated["hobbies"] == ["hiking", "biking"]
    assert person["hobbies"] == ["hiking"], \
        "The dictionary that was passed in must survive."
    assert updated is not person
