"""Interning is an optimization where the interpreter stores immutable copies of
commonly-used values, so it doesn't have to recreate them every time.

These behaviors are all implementation specific; they aren't guaranteed by the
reference.

The `id` function (in the reference implementation) gives the address in memory of its
argument. `a is b` is syntax sugar for `id(a) == id(b)`, and similarly for `is not` and
`!=`.
"""

from string import ascii_lowercase
import random

# String interning
foo = "Hello, world!"
bar = "Hello," + " " + "world!"
assert foo == bar
assert foo is bar

# Strings are only interned if computable at compile-time
foo = "Hello, world!"
bar = "".join(["Hello,", " ", "world!"])
assert foo == bar
assert foo is not bar

# But, all one-character strings are interned at compile time
random.seed(0)
foo = random.choice(ascii_lowercase)

random.seed(0)  # reset the seed to guarantee repeated randomizatoin
bar = random.choice(ascii_lowercase)

assert foo == bar
assert foo is bar


# Integer interning
foo = 256
bar = 256
assert foo == bar
assert foo is bar

# this would be false if typed into an interpreter, because python only interns from -5
# to 256 unless it knows at compile time other integers are used
foo = 257
bar = 257
assert foo == bar
assert foo is bar

# anything in this range is interned
random.seed(0)
foo = random.randint(-5, 257)

random.seed(0)
bar = random.randint(-5, 257)

assert foo == bar
assert foo is bar

# anything in this range is not interned
random.seed(0)
foo = random.randint(257, 1000)

random.seed(0)
bar = random.randint(257, 1000)

assert foo == bar
assert foo is not bar


# lists are mutable, so they cannot be interned
foo = []
bar = []
assert foo == bar
assert foo is not bar

# tuples are immutable, so they can be interned
foo = ()
bar = ()
assert foo == bar
assert foo is bar
