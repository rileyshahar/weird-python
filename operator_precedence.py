"""Operator precedence causing counterintuitive behavior."""

# the walrus operator doesn't support tuple unpacking
foo = 1, 2
assert foo == (1, 2)
assert (bar := 1, 2) == (1, 2)
assert bar == 1

# regardless of whether `==` or `in` have higher precedence, this is always false
assert not (False == False) in [False]
assert not False == (False in [False])

# but this is true, because chained comparison operators desugar weirdly:
# `a OP b OP c` becomes `(a OP b) and (b OP c)`, rather than normal precedence
# this allows writing nice things like `0 < x < 17`, but creates weird behavior in this
# case
assert False == False in [False]
