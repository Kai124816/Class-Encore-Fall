# 1
def find_book(books, power):
    """
    Finds the index of the book with the given 'power' value.
    Returns -1 if the book isn't found.

    >>> find_book([1, 5, 7, 12, 19, 21, 30, 33, 42], 21) # doctest: +SKIP
    5
    >>> find_book([1, 5, 7, 12, 19, 21, 30, 33, 42], 6) # doctest: +SKIP
    -1
    >>> find_book([], 10) # doctest: +SKIP
    -1
    """
    return

#2
def find_first_broken(mirrors):
    """
    Given a list like [True, True, True, False, False, False],
    returns the index of the FIRST broken mirror (first False).
    Returns -1 if all mirrors are working.

    >>> find_first_broken([True, True, True, False, False, False]) # doctest: +SKIP
    3
    >>> find_first_broken([True, True, True]) # doctest: +SKIP
    -1
    >>> find_first_broken([False, False, False]) # doctest: +SKIP
    0
    >>> find_first_broken([]) # doctest: +SKIP
    -1
    """
    return

#3
def sum_nested(numbers):
    """
    Recursively sums all integers in a list that may contain other lists.

    Examples (doctests):

    >>> sum_nested([1, 2, 3]) # doctest: +SKIP
    6
    >>> sum_nested([1, [2, 3], 4]) # doctest: +SKIP
    10
    >>> sum_nested([[1, [2]], [3, [4, [5]]]]) # doctest: +SKIP
    15
    >>> sum_nested([]) # doctest: +SKIP
    0
    >>> sum_nested([[], [[], []]]) # doctest: +SKIP
    0
    """
    return

#4 
DigSite = str | list['DigSite']

def calculate_worth(site: DigSite) -> int:
    """Returns the total worth of the dig site. Gold is worth 10 and 
    diamonds are worth 20

    >>> calculate_worth("gold") # doctest: +SKIP
    10
    >>> calculate_worth(["diamond", ["gold", ["rocks", [], "gold"], "gold"], "gold"]) # doctest: +SKIP
    60
    >>> calculate_worth(["rocks", ["rocks", ["rocks", "rocks"], "rocks"], "rocks"]) # doctest: +SKIP
    0
    >>> calculate_worth(["diamond", ["diamond", ["gold", "diamond"]]]) # doctest: +SKIP
    70
    """
    return

#5
def consult_oracle(runes: list[int], number: int) -> bool:
    """Returns True if 'number' is found in the sorted list 'runes', else False.
    Must use recursion

    >>> consult_oracle([1, 3, 5, 7, 9, 11], 7) # doctest: +SKIP
    True
    >>> consult_oracle([1, 3, 5, 7, 9, 11], 8) # doctest: +SKIP
    False
    >>> consult_oracle([], 5) # doctest: +SKIP
    False
    >>> consult_oracle([10], 10) # doctest: +SKIP
    True
    """
    return

if __name__ == "__main__":
    import doctest
    doctest.testmod()
