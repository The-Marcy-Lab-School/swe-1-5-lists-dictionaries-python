# Lists and Dictionaries

Practice storing collections of data, reaching into them, and knowing when a
function changes what it was given.

**Practicing:** lists, dictionaries, records, lookup tables, references, copying

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Before You Start](#before-you-start)
- [From Scratch](#from-scratch)
  - [Question 1: `add_to_front_or_back`](#question-1-add_to_front_or_back)
  - [Question 2: `insert_into_middle`](#question-2-insert_into_middle)
  - [Question 3: `is_right_index`](#question-3-is_right_index)
  - [Question 4: `get_all_y_coordinates`](#question-4-get_all_y_coordinates)
  - [Question 5: `unpack_point`](#question-5-unpack_point)
  - [Question 6: `cool_greeting`](#question-6-cool_greeting)
  - [Question 7: `become_secret_agent`](#question-7-become_secret_agent)
  - [Question 8: `get_next_opponent`](#question-8-get_next_opponent)
  - [Question 9: `total_by_category`](#question-9-total_by_category)
- [Modify](#modify)
  - [Question 10: `add_guest`](#question-10-add_guest)
  - [Question 11: `get_passing_students`](#question-11-get_passing_students)
- [Debug](#debug)
  - [Question 12: `get_first_item`](#question-12-get_first_item)
  - [Question 13: `we_are_not_friends`](#question-13-we_are_not_friends)
  - [Question 14: `change_email`](#question-14-change_email)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine,
and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you
write every line you submit. For this assignment that means asking it what
happens when two names point at the same list, or having it quiz you on
`.get()` versus bracket notation until you can say when each one is right.
Ask it a hundred questions — that is the whole point. What you do not do is
ask it for the function. Paste this at the start of a chat and it will hold
for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from
it, and then you verify that code line by line. For this assignment your spec
has to say, for every function, whether it changes what it was given or hands
back something new. If what comes back does more than you asked for, reject
it — over-delivery is a defect, and catching it is part of the job.

You own every line either way, and you will be asked to explain it.

## Setup

Clone your repository in `development/mod-1` and then `cd` into it. Set up
your virtual environment and make a draft branch before you start.

```sh
git clone [your_repo]
cd [your_repo]
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` to test the entire assignment, or `pytest -k cool_greeting` for
one question. Every push runs the tests on GitHub and reports your score in
the **Actions** tab.

75% of tests passing counts as complete. Submit at that point even if it is
not perfect. Treat submitting as a checkpoint rather than a finish line, and
come back to improve it.

When you are done working on this assignment, turn off your virtual
environment by running:

```sh
deactivate
```

## Before You Start

This assignment has three sections:

1. From Scratch
2. Modify
3. Debug

You will write functions that take parameters, return values, and loop. None
of that is the new material. If any of it still feels shaky, take time to
study it first, because fighting the syntax and a new idea at once is twice as
hard.

Every question that works with a collection either **changes the collection
it was given** or **hands back something new**, and the tests check which.
**Read each question for which one it wants before you write anything.**

## From Scratch

Write your solutions in `src/from_scratch.py`.

### Question 1: `add_to_front_or_back`

Write a function `add_to_front_or_back` that takes a list `items`, a `value`,
and a boolean `to_front`. It should add the value to the front when
`to_front` is `True` and to the back otherwise. It returns nothing.

```python
items = ["b", "c"]
add_to_front_or_back(items, "a", True)
# items is now ["a", "b", "c"] — "a" went to the front
add_to_front_or_back(items, "d", False)
# items is now ["a", "b", "c", "d"] — "d" went to the back
```

This function **changes the list it was given**, which is why it returns
nothing. There are two list methods here, one for each end. Can you find both
in the
[list methods reference](https://www.w3schools.com/python/python_lists_methods.asp)?

### Question 2: `insert_into_middle`

Write a function `insert_into_middle` that takes a list `items` and a `value`,
and puts the value in the middle. It returns nothing.

```python
even = [1, 2, 3, 4]
insert_into_middle(even, "x")
# [1, 2, "x", 3, 4] — four items, so "x" lands at position 2
odd = [1, 2, 3]
insert_into_middle(odd, "x")
# [1, "x", 2, 3] — three items, so "x" lands at position 1
```

An odd-length list has no exact middle. Work out from the two examples which
way this one rounds, then find the division that does it in one step.

### Question 3: `is_right_index`

Write a function `is_right_index` that takes a list `items`, an `index`, and a
`value`. It returns `True` when that position holds that value.

```python
items = ["a", "b", "c"]
is_right_index(items, 0, "a")
# True — position 0 does hold "a"
is_right_index(items, 1, "c")
# False — position 1 holds "b", not "c"
is_right_index(items, 9, "c")
# False — there is no position 9, and that is an answer, not a crash
```

That last case is the whole question. Reaching for a position that does not
exist raises an `IndexError`, so check before you reach.

### Question 4: `get_all_y_coordinates`

Write a function `get_all_y_coordinates` that takes a list of points and
returns a **new** list of just the second number from each.

```python
get_all_y_coordinates([[1, 2], [3, 4]])
# [2, 4] — the second number of each pair
get_all_y_coordinates([])
# [] — nothing in, nothing out
```

Each point is a small list inside a bigger one, so you are reaching two
levels down: once for the point, once for the number inside it.

### Question 5: `unpack_point`

Write a function `unpack_point` that takes one point and returns a sentence
about it.

```python
unpack_point([3, 4])
# "x is 3, y is 4"
unpack_point([0, -2])
# "x is 0, y is -2"
```

You could reach in by position twice. Instead, **unpack** it: Python can
assign several names at once from one list.

```py
first, second = some_pair
```

### Question 6: `cool_greeting`

Write a function `cool_greeting` that takes a `person` dictionary and returns
a greeting that depends on the `is_cool` key.

```python
cool_greeting({"name": "Sara", "is_cool": True})
# "What is UP SARA? How you been doin'?" — the cool version shouts the name
cool_greeting({"name": "Bob", "is_cool": False})
# "Greetings Bob, how have you been lately?"
cool_greeting({"name": "Zo", "is_cool": True, "age": 30})
# "What is UP ZO? How you been doin'?" — the extra key is ignored
```

That third case matters. A function should read only the keys it needs, so a
caller can hand it a bigger dictionary without anything breaking.

### Question 7: `become_secret_agent`

Write a function `become_secret_agent` that takes a `person` dictionary and a
`spy_handle` string. It removes the `"name"` key entirely and adds a
`spy_handle` key. It changes the dictionary and returns nothing.

```python
person = {"name": "Sara", "age": 30}
become_secret_agent(person, "007")
# person is now {"age": 30, "spy_handle": "007"} — "name" is gone, not blanked
```

No trace of the old name can be left, so setting it to `None` will not do. If
you are stuck, ask your AI tutor in **tutor mode** how removing a key differs
from blanking its value. Make it explain the idea rather than hand you the
line.

### Question 8: `get_next_opponent`

Write a function `get_next_opponent` that takes a `team` dictionary and
returns the `team_name` of the first match, or `None` when there are no
matches left.

```python
fighters = {
    "name": "Fighters",
    "matches": [
        {"team_name": "Dunkaroos", "skill": 9},
        {"team_name": "Space Jammers", "skill": 10},
    ],
}

get_next_opponent(fighters)
# "Dunkaroos" — the first match's team_name
get_next_opponent({"name": "Lonely", "matches": []})
# None — no matches left to play
```

The value you want is nested three deep: a dictionary, holding a list,
holding more dictionaries. Take it one step at a time and print what you have
as you go.

### Question 9: `total_by_category`

Write a function `total_by_category` that takes a list of expense records and
returns a **new** dictionary that maps each category to the total amount spent
in it.

```python
expenses = [
    {"category": "food", "amount": 12.50},
    {"category": "rent", "amount": 900},
    {"category": "food", "amount": 8.25},
    {"category": "rent", "amount": 100},
]

total_by_category(expenses)
# {"food": 20.75, "rent": 1000}
total_by_category([])
# {} — no expenses, so no categories
```

`expenses` is a list of records: every expense has the same two keys. The
dictionary you return is a lookup table: every key is a category, and every
value is that category's total.

Start with an empty dictionary. The first time a category appears, it is not a
key yet, so think about which way of reading a value can handle a missing key.

## Modify

Change the two functions already in `src/modify.py`.

### Question 10: `add_guest`

`add_guest` should return a guest list with one more name on it. It returns
the right list, but it also adds the name to the list it was given.

```python
friday = ["Ada", "Zo"]
saturday = add_guest(friday, "Maya")
# saturday is ["Ada", "Zo", "Maya"] — correct
# friday is ALSO ["Ada", "Zo", "Maya"] — wrong, Maya was only invited on Saturday
```

Change `add_guest` so that `friday` stays `["Ada", "Zo"]`. Making a function
leave its input alone is usually one line: copy first, then work on the copy.

The test checks that what comes back is a **different list** from the one that
went in, not just that the names look right.

### Question 11: `get_passing_students`

`get_passing_students` takes a `grades` dictionary and a `passing_score`, and
returns the names of every student whose score is at least `passing_score`.

```python
grades = {"Ada": 92, "Zo": 61, "Maya": 75}
get_passing_students(grades, 70)
# ["Ada", "Maya"] — Zo's 61 is below 70
```

`grades` is a lookup table: every key is a student, and every value is that
student's score. The function works, but its loop is handed only each name, so
it has to look up the score again with `grades[name]`.

Rewrite the loop with `.items()`, so that the loop hands you each name and its
score together. The tests check that your loop uses `.items()`.

## Debug

Fix the three functions in `src/debug.py`.

### Question 12: `get_first_item`

`get_first_item` should return the first item, or `None` when the list is
empty. It raises an `IndexError` on an empty list instead.

```python
get_first_item(["a", "b"])   # "a"
get_first_item([])           # IndexError, want None
```

### Question 13: `we_are_not_friends`

`we_are_not_friends` should remove and return the **last** friend. It removes
the first one, and raises an `IndexError` when there are no friends at all.

```python
person = {"name": "Sara", "friends": ["Bob", "Joe", "Sally"]}
we_are_not_friends(person)
# want "Sally", gets "Bob"
```

Two things to fix, and the tests check both.

### Question 14: `change_email`

`change_email` should return a copy of an account with a new email, and leave
the original account alone. However, it currently changes the original too.

```python
account = {"name": "Ada", "email": "ada@old.com"}
updated = change_email(account, "ada@new.com")
# updated["email"] is "ada@new.com" — correct
# account["email"] is ALSO "ada@new.com" — wrong, it should still be "ada@old.com"
```

The test checks that what comes back is a **different dictionary** from the
one that went in, not just that the email in the returned record looks right.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Pushing runs the tests on GitHub. Check the **Actions** tab for your score,
then open a pull request to your instructor for feedback.

## Good luck!

Lists and dictionaries are how almost all real data arrives, so this is the
assignment that starts paying off immediately. You got this!
