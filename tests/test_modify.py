import ast
import inspect
import textwrap

from modify import add_guest, get_passing_students

TEST_SUITE_NAME = "Modify Tests"


def methods_called_in(func):
    """The names of the methods a function calls, such as "items" for grades.items().

    The function's code is read with Python's ast module rather than searched as
    text, so words in comments and strings never count. A comment that says
    "use .items() here" does not count as calling .items().
    """
    source = textwrap.dedent(inspect.getsource(func))
    methods = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            methods.add(node.func.attr)
    return methods


def test_add_guest_leaves_the_original_alone():
    """add_guest - returns a new guest list and leaves the original alone"""
    friday = ["Ada", "Zo"]
    saturday = add_guest(friday, "Maya")

    assert saturday == ["Ada", "Zo", "Maya"]
    assert friday == ["Ada", "Zo"], "The list that was passed in must survive."
    assert saturday is not friday
    assert add_guest([], "Ada") == ["Ada"]


def test_get_passing_students_uses_items():
    """get_passing_students - returns the passing names, using .items() in the loop"""
    grades = {"Ada": 92, "Zo": 61, "Maya": 75}
    assert get_passing_students(grades, 70) == ["Ada", "Maya"]
    assert get_passing_students(grades, 75) == ["Ada", "Maya"]
    assert get_passing_students(grades, 100) == []
    assert get_passing_students({}, 70) == []

    assert "items" in methods_called_in(get_passing_students), \
        "Rewrite the loop so that .items() hands you each name and score together."
