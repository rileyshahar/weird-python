"""Weird behavior as a result of Python's support for unicode identifiers."""

# unicode normlaization: different symbols normalize to the same value
# https://www.asmeurer.com/python-unicode-variable-names/
ª = 1
assert a == 1

# symbols that look identical (in many fonts) but are not normalized properly
j = 2
ј = 3
assert j == 2
assert ј == 3
