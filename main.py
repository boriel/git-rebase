# -*- coding: utf-8 -*-

""" The first comment in a module is the module docstring.
If you print mymodule.__doc__ its value is this comment.

When no docstring is specified, __doc__ equals to None
"""

HELP = """
Repeating Things
----------------

Being able to match varying sets of characters is the first thing regular
expressions can do that isn't already possible with the methods available on
strings.  However, if that was the only additional capability of regexes, they
wouldn't be much of an advance. Another capability is that you can specify that
portions of the RE must be repeated a certain number of times.

The first metacharacter for repeating things that we'll look at is ``*``.  ``*``
doesn't match the literal character ``'*'``; instead, it specifies that the
previous character can be matched zero or more times, instead of exactly once.

For example, ``ca*t`` will match ``'ct'`` (0 ``'a'`` characters), ``'cat'`` (1 ``'a'``),
``'caaat'`` (3 ``'a'`` characters), and so forth.

A step-by-step example will make this more obvious.  Let's consider the
expression ``a[bcd]*b``.  This matches the letter ``'a'``, zero or more letters
from the class ``[bcd]``, and finally ends with a ``'b'``.  Now imagine matching
this RE against the string ``'abcbd'``.
"""