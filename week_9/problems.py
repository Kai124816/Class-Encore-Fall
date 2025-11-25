import doctest

#Problem 1
def locate_item(target: int, L: list[int]) -> int:
    """
    Finds the index of 'target' in the sorted list 'L' using binary search.
    Returns the index if found, otherwise returns -1.
    
    >>> locate_item(30, [10, 20, 30, 40, 50]) # doctest: +SKIP
    2
    >>> locate_item(10, [10, 20, 30, 40, 50]) # doctest: +SKIP
    0
    >>> locate_item(55, [10, 20, 30, 40, 50]) # doctest: +SKIP
    -1
    >>> locate_item(7, [10, 20, 30, 40, 50]) # doctest: +SKIP
    -1
    """

#Problem 2

# The structure of the group_map is: item -> (group_name, value)
GROUP_DATA = {
    "apple": ("fruit", 10),
    "banana": ("fruit", 5),
    "carrot": ("vegetable", 8),
    "steak": ("meat", 50),
    "chicken": ("meat", 35)
}

def sum_by_group(items: list[str], group_map: dict[str, tuple[str, int]]) -> dict[str, int]:
    """
    Calculates the total numerical value for each group based on the input items.
    
    >>> items_list_1 = ["apple", "banana", "steak", "apple", "toast"]
    >>> sum_by_group(items_list_1, GROUP_DATA) # doctest: +SKIP
    {'fruit': 25, 'meat': 50}
    
    >>> items_list_2 = ["carrot", "chicken", "carrot"]
    >>> sum_by_group(items_list_2, GROUP_DATA) # doctest: +SKIP
    {'vegetable': 16, 'meat': 35}
    """

TREASURE_GRID = [
    ["X", "X", "X", "X", "X"],
    ["X", ".", ".", ".", "X"],
    ["X", ".", "X", ".", "X"],
    ["X", ".", "X", "T", "X"],
    ["X", "X", "X", "X", "X"]
]

#Problem 3
def find_treasure(grid: list[list[str]], row: int, col: int) -> bool:
    """
    Checks if a path exists from (row, col) to the 'T' cell.
    Modifies the grid in place to mark visited cells.
    
    >>> find_treasure(TREASURE_GRID, 1, 1) # doctest: +SKIP
    True
    
    # A new, modified grid for the next test
    >>> IMPASSABLE_GRID = [
    ...     ["X", "X", "X", "X", "X"],
    ...     ["X", ".", "X", ".", "X"],
    ...     ["X", ".", "X", ".", "X"],
    ...     ["X", "T", "X", ".", "X"],
    ...     ["X", "X", "X", "X", "X"]
    ... ]
    >>> find_treasure(IMPASSABLE_GRID, 1, 3) # doctest: +SKIP
    False
    """

#Problem 4
def unique_neighbors(li: list[int]) -> list[int]:
    """
    Returns a new list containing elements from li that are different from 
    at least one of their immediate neighbors.
    
    >>> unique_neighbors([1, 1, 2, 2, 2, 3, 3, 4, 1]) # doctest: +SKIP
    [1, 2, 2, 3, 3, 4, 1]
    
    # Explanation:
    # Index 0 (1): Different from neighbor (1) is False. Skip.
    # Index 1 (1): Different from neighbor (2) is True. Keep.
    # Index 2 (2): Different from neighbor (1) or (2) is True. Keep.
    # Index 3 (2): Different from neighbor (2) is False. Skip.
    # Index 4 (2): Different from neighbor (3) is True. Keep.
    # Index 5 (3): Different from neighbor (2) or (3) is True. Keep.
    # Index 6 (3): Different from neighbor (4) is True. Keep.
    # Index 7 (4): Different from neighbor (3) or (1) is True. Keep.
    # Index 8 (1): Different from neighbor (4) is True. Keep.
    
    >>> unique_neighbors([5, 5, 5, 5]) # doctest: +SKIP
    []
    
    >>> unique_neighbors([10]) # doctest: +SKIP
    [10]
    """

#Problem 5
NESTED_DATA = {
    "A": 5,
    "B": {
        "C": 10,
        "D": {
            "E": 2,
            "F": 3
        }
    },
    "G": 1,
    "H": {}
}

def sum_nested_values(data: dict) -> int:
    """
    Recursively sums all integer values found in the nested dictionary structure.
    
    >>> sum_nested_values(NESTED_DATA) # doctest: +SKIP
    21
    
    >>> sum_nested_values({"one": 1, "two": {"a": 2}, "three": 3}) # doctest: +SKIP
    6
    """

#Problem 6
def find_local_peaks(data: list[int]) -> list[int]:
    """
    Returns a new list containing all elements from 'data' that are 
    local peaks (strictly greater than both immediate neighbors).
    
    >>> find_local_peaks([1, 5, 2, 8, 8, 6, 9, 3]) # doctest: +SKIP
    [5, 9]
    
    >>> find_local_peaks([10, 2, 20, 5, 30]) # doctest: +SKIP
    [10, 20, 30]
    
    >>> find_local_peaks([7]) # doctest: +SKIP
    [7]
    
    >>> find_local_peaks([5, 5, 5]) # doctest: +SKIP
    []
    """
    # Your implementation goes here.

if __name__ == "__main__":
    doctest.testmod()