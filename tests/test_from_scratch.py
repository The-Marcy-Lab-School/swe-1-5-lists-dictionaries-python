from from_scratch import (
    add_to_front_or_back,
    become_secret_agent,
    cool_greeting,
    get_all_y_coordinates,
    get_next_opponent,
    insert_into_middle,
    is_right_index,
    unpack_point,
)

TEST_SUITE_NAME = "From Scratch Tests"


def test_add_to_front_or_back():
    """add_to_front_or_back - changes the list it was given, returns nothing"""
    items = ["b", "c"]
    assert add_to_front_or_back(items, "a", True) is None
    assert items == ["a", "b", "c"]

    add_to_front_or_back(items, "d", False)
    assert items == ["a", "b", "c", "d"]


def test_insert_into_middle():
    """insert_into_middle - puts the value in the middle, changing the list"""
    even = [1, 2, 3, 4]
    assert insert_into_middle(even, "x") is None
    assert even == [1, 2, "x", 3, 4]

    odd = [1, 2, 3]
    insert_into_middle(odd, "x")
    assert odd == [1, "x", 2, 3]


def test_is_right_index():
    """is_right_index - True when that position holds that value"""
    items = ["a", "b", "c"]
    assert is_right_index(items, 0, "a") is True
    assert is_right_index(items, 2, "c") is True
    assert is_right_index(items, 1, "c") is False
    # A position past the end is a question, not a crash.
    assert is_right_index(items, 9, "c") is False


def test_get_all_y_coordinates():
    """get_all_y_coordinates - pulls the second number out of each pair"""
    assert get_all_y_coordinates([(1, 2), (3, 4)]) == [2, 4]
    assert get_all_y_coordinates([(0, 0)]) == [0]
    assert get_all_y_coordinates([]) == []


def test_unpack_point():
    """unpack_point - unpacks a point into a message"""
    assert unpack_point((3, 4)) == "x is 3, y is 4"
    assert unpack_point((0, -2)) == "x is 0, y is -2"


def test_cool_greeting():
    """cool_greeting - reads only the keys it needs"""
    assert cool_greeting({"name": "Sara", "is_cool": True}) == \
        "What is UP SARA? How you been doin'?"
    assert cool_greeting({"name": "Bob", "is_cool": False}) == \
        "Greetings Bob, how have you been lately?"
    # Extra keys are none of this function's business.
    assert cool_greeting({"name": "Zo", "is_cool": True, "age": 30}) == \
        "What is UP ZO? How you been doin'?"


def test_become_secret_agent():
    """become_secret_agent - removes a key and adds another, in place"""
    person = {"name": "Sara", "age": 30}
    assert become_secret_agent(person, "007") is None
    assert person == {"age": 30, "spy_handle": "007"}
    assert "name" not in person


def test_get_next_opponent():
    """get_next_opponent - reaches three levels into the data"""
    fighters = {
        "name": "Fighters",
        "matches": [
            {"team_name": "Dunkaroos", "skill": 9},
            {"team_name": "Space Jammers", "skill": 10},
        ],
    }
    assert get_next_opponent(fighters) == "Dunkaroos"
    assert get_next_opponent({"name": "Lonely", "matches": []}) is None
