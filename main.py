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

Repetitions such as ``*`` are :dfn:`greedy`; when repeating a RE, the matching
engine will try to repeat it as many times as possible. If later portions of the
pattern don't match, the matching engine will then back up and try again with
fewer repetitions.

A step-by-step example will make this more obvious.  Let's consider the
expression ``a[bcd]*b``.  This matches the letter ``'a'``, zero or more letters
from the class ``[bcd]``, and finally ends with a ``'b'``.  Now imagine matching
this RE against the string ``'abcbd'``.

+------+-----------+---------------------------------+
| Step | Matched   | Explanation                     |
+======+===========+=================================+
| 1    | ``a``     | The ``a`` in the RE matches.    |
+------+-----------+---------------------------------+
| 2    | ``abcbd`` | The engine matches ``[bcd]*``,  |
|      |           | going as far as it can, which   |
|      |           | is to the end of the string.    |
+------+-----------+---------------------------------+
| 3    | *Failure* | The engine tries to match       |
|      |           | ``b``, but the current position |
|      |           | is at the end of the string, so |
|      |           | it fails.                       |
+------+-----------+---------------------------------+
| 4    | ``abcb``  | Back up, so that  ``[bcd]*``    |
|      |           | matches one less character.     |
+------+-----------+---------------------------------+

Another repeating metacharacter is ``+``, which matches one or more times.  Pay
careful attention to the difference between ``*`` and ``+``; ``*`` matches
*zero* or more times, so whatever's being repeated may not be present at all,
while ``+`` requires at least *one* occurrence.  To use a similar example,
``ca+t`` will match ``'cat'`` (1 ``'a'``), ``'caaat'`` (3 ``'a'``\ s), but won't
match ``'ct'``.
"""