import doctest

# Problem 1: Binary Search
def locate_item(target: int, L: list[int]) -> int:
    """
    Finds the index of 'target' in the sorted list 'L' using binary search.
    Returns the index if found, otherwise returns -1.
    """
    high = len(L) - 1 # Initialize the upper bound of the search range (last index)
    low = 0          # Initialize the lower bound of the search range (first index)
    found = -1       # Default return value if the target is not found

    # Continue searching as long as the search range is valid (low index is not past high index)
    while high >= low:
        # Calculate the middle index of the current search range
        mid = (high + low) // 2

        # Case 1: Target is in the upper half
        if L[mid] < target:
            # Move the lower bound to 'mid + 1' to exclude the current middle element
            low = mid + 1
        # Case 2: Target is found
        elif L[mid] == target:
            return mid
        # Case 3: Target is in the lower half
        else:
            # Move the upper bound to 'mid - 1' to exclude the current middle element
            high = mid - 1
    
    # If the loop finishes without finding the target, return the default value
    return found

# Problem 2: Dictionary Aggregation

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
    """
    group_dict = {} # Initialize an empty dictionary to store the running totals for each group

    # Iterate through every item name in the input list
    for item in items:
        # Check if the current item is defined in the mapping dictionary
        if item in group_map:
            # Retrieve the (group_name, value) tuple from the map
            group, group_val = group_map[item]
            
            # If the group already exists in the totals dictionary, add the value
            if group in group_dict:
                group_dict[group] += group_val
            # Otherwise, initialize the group total with the current item's value
            else:
                group_dict[group] = group_val
    
    return group_dict # Return the final totals dictionary
    
# Problem 3: Depth-First Search (DFS) for Pathfinding
TREASURE_GRID = [
    ["X", "X", "X", "X", "X"],
    ["X", ".", ".", ".", "X"],
    ["X", ".", "X", ".", "X"],
    ["X", ".", "X", "T", "X"],
    ["X", "X", "X", "X", "X"]
]

def find_treasure_corrected(grid: list[list[str]], row: int, col: int) -> bool:
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    # --- Base Cases (When the path terminates) ---
    
    # 1. Out of Bounds Check: If the current position is outside the grid, it's a dead end.
    if not (0 <= row < num_rows and 0 <= col < num_cols):
        return False
        
    # 2. Wall/Visited Check: If the cell is a wall ('X') or was already visited, it's a dead end.
    if grid[row][col] == 'X':
        return False
        
    # 3. Success Check: If the cell contains the treasure ('T'), a path is found.
    if grid[row][col] == 'T':
        return True
    
    # --- Recursive Step (Exploration) ---
    
    # Mark the current cell as visited to prevent immediate cycles and re-visiting.
    # This is crucial for successful pathfinding with DFS.
    grid[row][col] = 'X' 
    
    # Try all four possible directions. If any recursive call finds the treasure, return True immediately.
    
    # Check Up (row - 1)
    if find_treasure_corrected(grid, row - 1, col): 
        return True
        
    # Check Down (row + 1)
    if find_treasure_corrected(grid, row + 1, col): 
        return True
        
    # Check Left (col - 1)
    if find_treasure_corrected(grid, row, col - 1): 
        return True
        
    # Check Right (col + 1)
    if find_treasure_corrected(grid, row, col + 1): 
        return True
    
    # If all four directions return False, no path exists from this cell.
    return False 

# Problem 4: Filtering by Neighbor Difference
def unique_neighbors(li: list[int]) -> list[int]:
    """
    Returns a new list containing elements from li that are different from 
    at least one of their immediate neighbors.
    """
    n = len(li)
    if n == 1:
        return li # A single element has no neighbors, but is kept per the test case.
    
    unique_list = []

    # Iterate through all elements by index
    for i in range(n):
        curr_el = li[i]
        
        # Check if the left neighbor exists and is different from the current element
        # i > 0 ensures we are not at the first index (0)
        left_differs = (i > 0) and (li[i - 1] != curr_el)
        
        # Check if the right neighbor exists and is different from the current element
        # i < n - 1 ensures we are not at the last index
        right_differs = (i < n - 1) and (li[i + 1] != curr_el)

        # Append the current element if it differs from AT LEAST ONE of its neighbors
        if left_differs or right_differs:
            unique_list.append(curr_el)

    return unique_list

# Problem 5: Recursive Dictionary Summation
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
    """
    total = 0

    # Iterate over key-value pairs in the dictionary
    for key, value in data.items():
        # Check if the value is an integer
        if isinstance(value, int):
            # If it's an integer, add it to the running total
            total += value
        # If the value is another dictionary (nested structure)
        else:
            # Recursively call the function to sum the values in the nested dictionary
            total += sum_nested_values(value)

    return total # Return the total sum for this level and all sub-levels

# Problem 6: Detecting Local Peaks
def find_local_peaks(data: list[int]) -> list[int]:
    """
    Returns a new list containing all elements from 'data' that are 
    local peaks (strictly greater than both immediate neighbors, or its one neighbor for boundaries).
    """
    n = len(data)
    if n == 1:
        return data # Single element is trivially a peak.
    
    peaks = []

    # 1. Check the first element (Index 0)
    # It only has a right neighbor (Index 1)
    if data[0] > data[1]:
        peaks.append(data[0])

    # 2. Check interior elements (Indices 1 to n-2)
    for i in range(1, n - 1):
        curr_el = data[i]
        # Check if the current element is strictly greater than BOTH its left and right neighbors
        if curr_el > data[i - 1] and curr_el > data[i + 1]:
            peaks.append(curr_el)
    
    # 3. Check the last element (Index n-1)
    # It only has a left neighbor (Index n-2)
    if data[n - 1] > data[n - 2]:
        peaks.append(data[n - 1])

    return peaks

if __name__ == "__main__":
    doctest.testmod()