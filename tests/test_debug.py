from debug import (
    add_hobby,
    get_first_item,
    group_by_location,
    set_first_item,
    set_first_letter,
    we_are_not_friends,
)

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


def test_add_hobby_leaves_the_original_alone():
    """add_hobby - returns a new person and leaves the original alone"""
    person = {"name": "Sara", "hobbies": ["hiking"]}
    updated = add_hobby(person, "biking")

    assert updated["hobbies"] == ["hiking", "biking"]
    assert person["hobbies"] == ["hiking"], \
        "The dictionary that was passed in must survive."
    assert updated is not person


def test_set_first_item_already_works():
    """set_first_item - replaces the first item of a list"""
    items = ["a", "b", "c"]
    assert set_first_item(items, "z") == ["z", "b", "c"]


def test_set_first_letter():
    """set_first_letter - returns the word with its first letter replaced"""
    assert set_first_letter("ada", "A") == "Ada"
    assert set_first_letter("zo", "Z") == "Zo"
    assert set_first_letter("b", "B") == "B"


def test_set_first_letter_leaves_the_original_alone():
    """set_first_letter - the word that went in is unchanged"""
    word = "ada"
    set_first_letter(word, "A")
    assert word == "ada"


def test_group_by_location():
    """group_by_location - counts people by city and country"""
    people = [
        {"name": "Ada", "city": "NYC", "country": "US"},
        {"name": "Zo", "city": "NYC", "country": "US"},
        {"name": "Bo", "city": "Leeds", "country": "UK"},
    ]
    assert group_by_location(people) == {("NYC", "US"): 2, ("Leeds", "UK"): 1}
    assert group_by_location([]) == {}
