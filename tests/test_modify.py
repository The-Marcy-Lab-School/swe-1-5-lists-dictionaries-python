from modify import clear_list, count_by_owner, have_birthday

TEST_SUITE_NAME = "Modify Tests"


def test_clear_list_leaves_the_original_alone():
    """clear_list - returns an empty list and leaves the original alone"""
    items = ["a", "b", "c"]
    assert clear_list(items) == []
    assert items == ["a", "b", "c"], "The list that was passed in must survive."


def test_have_birthday():
    """have_birthday - adds one to the age inside the dictionary"""
    person = {"name": "Sara", "age": 30}
    assert have_birthday(person) is None
    assert person["age"] == 31

    have_birthday(person)
    assert person["age"] == 32


def test_count_by_owner():
    """count_by_owner - counts each owner's pets using items()"""
    pets = {"Ada": ["cat", "dog"], "Zo": ["newt"]}
    assert count_by_owner(pets) == {"Ada": 2, "Zo": 1}
    assert count_by_owner({}) == {}
