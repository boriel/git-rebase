# -*- coding: utf-8 -*-

""" The first comment in a module is the module docstring.
If you print mymodule.__doc__ its value is this comment.

When no docstring is specified, __doc__ equals to None
"""

HELP = """
REGULAR EXPRESSIONS 

Introduction
============

1. Regular expressions (called REs, or regexes, or regex patterns) are essentially
a tiny, highly specialized programming language embedded inside Python and made
available through the :mod:`re` module. Using this little language, you specify
the rules for the set of possible strings that you want to match; this set might
contain English sentences, or e-mail addresses, or TeX commands, or anything you
like.  You can then ask questions such as "Does this string match the pattern?",
or "Is there a match for the pattern anywhere in this string?".  You can also
use REs to modify a string or to split it apart in various ways.

Regular expression patterns are compiled into a series of bytecodes which are
then executed by a matching engine written in C.  For advanced use, it may be
necessary to pay careful attention to how the engine will execute a given RE.
"""
