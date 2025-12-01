import doctest

#Problem 1 (What does this print)
def h(a: int) -> int:
    b = a + 4
    return b

def i(b: int) -> int:
    a = h(b) * 2
    return a

a = 10
b = 5
c = i(a)
#Uncomment these to check answer
# print(a) 
# print(b)
# print(c)

#Problem 2
def filter_by_range(data: list[int], low: int, high: int) -> list[int]:
    """
    Returns a list containing elements from data such that low < element <= high.
    
    >>> filter_by_range([10, 25, 5, 30, 15, 25], 10, 25) # doctest: +SKIP
    [25, 15, 25]
    >>> filter_by_range([5, 8, 10, 12], 0, 5) # doctest: +SKIP
    [5]
    """
    return

#Problem 3
def match_at(m: list[int], n: list[int]) -> int:
    """
    Returns the smallest index i such that m[i] == n[i], or -1 if none exists.
    
    >>> match_at([10, 20, 30, 40], [40, 20, 10]) # doctest: +SKIP
    1
    >>> match_at([5, 8, 2], [5, 9, 3, 1]) # doctest: +SKIP
    0
    >>> match_at([1, 2], [3, 4]) # doctest: +SKIP
    -1
    """
    return
    

#Problem 4
def get_unique_multiples(li: list[str]) -> list[str]:
    """
    Returns a list of unique strings from li that appear exactly twice.
    
    >>> get_unique_multiples(["apple", "banana", "apple", "orange", "banana", "grape", "apple"]) # doctest: +SKIP
    ['banana'] 
    >>> get_unique_multiples(["a", "b", "c", "b", "c", "a"]) # doctest: +SKIP
    ['a', 'b', 'c']
    """
    return

#Problem 5
def dict_sum_safe(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Returns a dict with the combined nutrient counts from d1 and d2.
    
    >>> d1 = {'a': 1, 'b': 2}
    >>> d2 = {'b': 5, 'c': 3}
    >>> dict_sum_safe(d1, d2) # doctest: +SKIP
    {'a': 1, 'b': 7, 'c': 3}
    >>> dict_sum_safe({'x': 10}, {'y': 20}) # doctest: +SKIP
    {'x': 10, 'y': 20}
    """
    return

#Problem 6
def find_index_binary(target: int, sorted_data: list[int]) -> int:
    """
    Finds the index of the target in a sorted list using binary search.
    Returns -1 if the target is not found.
    
    >>> find_index_binary(5, [1, 3, 5, 7, 9]) # doctest: +SKIP
    2
    >>> find_index_binary(10, [1, 3, 5, 7, 9]) # doctest: +SKIP
    -1
    >>> find_index_binary(1, [1]) # doctest: +SKIP
    0
    """
    return

#Problem 7
def char_score(word: str, values: dict[str, int]) -> int:
    """
    Calculates the total score of a word based on character values.
    
    >>> char_score("hello", {'h': 1, 'e': 2, 'l': 3, 'o': 4}) # doctest: +SKIP
    13
    >>> char_score("python", {'p': 10, 'y': 20}) # doctest: +SKIP
    30
    """
    return

#Problem 8
def count_item(mine, item: str) -> int:
    """
    Recursively counts the occurrences of 'item' in the nested structure 'mine'.
    
    >>> count_item(['dirt', ['gold', ['rocks', 'gold'], 'rocks'], 'rocks'], 'gold') # doctest: +SKIP
    2
    >>> count_item('apple', 'apple') # doctest: +SKIP
    1
    >>> count_item(['a', ['b', ['c']]], 'd') # doctest: +SKIP
    0
    """
    return
    
#Problem 9
NETWORK = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": ["C"], # Loop: F can go back to C
    "G": ["H"]
}

#You can add to a set by using set.add(item)
def can_reach(start_node: str, end_node: str, visited: set) -> bool:
    """
    Recursively determines if end_node is reachable from start_node 
    in the NETWORK.

    The 'visited' set is used to track nodes already explored in the current path.
    
    >>> can_reach("A", "F", set()) # doctest: +SKIP
    True
    >>> can_reach("A", "H", set()) # doctest: +SKIP
    False
    >>> can_reach("B", "E", set()) # doctest: +SKIP
    True
    >>> can_reach("G", "A", set()) # doctest: +SKIP
    False
    """
    return

if __name__ == "__main__":
    doctest.testmod()