"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""
def strip_non_brackets(phrase):
    new_phrase = ''
    for char in phrase:
        if char in '{}()<>[]':
            new_phrase += char
    #print new_phrase
    return new_phrase


def find_matching_pair(phrase):
    if "()" in phrase:
        return "()"
    elif "[]" in phrase:
        return "[]"
    elif "<>" in phrase:
        return "<>"
    elif "{}" in phrase:
        return "{}"
    else:
        return None        


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """
    phrase = strip_non_brackets(phrase)
    #if phrase.count("{") != phrase.count("}") or phrase.count("(") != phrase.count(")") or phrase.count("[") != phrase.count("]") or phrase.count("<") != phrase.count(">"):
        #return False

    #while find_matching_pair(phrase) is not None:
    #    phrase = phrase.replace(find_matching_pair(phrase), '')
    pair = find_matching_pair(phrase)
    while pair is not None:
        phrase = phrase.replace(pair, '')
        pair = find_matching_pair(phrase)
    if len(phrase) > 0:
        return False
    else:
        return True




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n"
