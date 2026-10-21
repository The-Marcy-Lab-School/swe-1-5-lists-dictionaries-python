from debug import change_email, get_first_item, we_are_not_friends

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


def test_change_email_leaves_the_original_alone():
    """change_email - returns a new account and leaves the original alone"""
    account = {"name": "Ada", "email": "ada@old.com", "is_member": True}
    updated = change_email(account, "ada@new.com")

    assert updated == {"name": "Ada", "email": "ada@new.com", "is_member": True}
    assert account == {"name": "Ada", "email": "ada@old.com", "is_member": True}, \
        "The dictionary that was passed in must survive."
    assert updated is not account
