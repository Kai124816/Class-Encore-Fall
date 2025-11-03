#1 what does this print

def triple(n: int) -> int:
    n = n * 3
    return n

def shift(a: int, b: int) -> int:
    a = triple(a)
    b = a + b
    return b

x = 2
y = 5
z = shift(x, y)
# print(x)  //Uncomment print statements to test answers
# print(y)
# print(z)

#2 What does this print

LEVELS = [50, 20, 10, 0]
BONUS = [3, 2, 1.5, 1]

def scale(score: int) -> float:
    """Return scaled version of score"""
    for i in range(len(LEVELS)):
        if score >= LEVELS[i]:
            return score * BONUS[i]
    return 0.0

# print(scale(75)) //Uncomment print statements to test answers
# print(scale(12))
# print(scale(4))


# Note: For the complete this function problems remove the # doctest: +SKIP comment to run the doctests


#3 Complete function shorter_first consistent with its docstring and examples.

def shorter_first(a: list[str], b: list[str]) -> list[str]:
    """Return a list whose elements are the shorter of a[i] and b[i],
    for every index i that exists in both lists.
    Break ties in favor of b[i].
    
    >>> shorter_first(["bear", "cat", "alligator"], ["dog", "elephant", "ant"]) # doctest: +SKIP
    ['dog', 'cat', 'ant']
    >>> shorter_first(["hi", "there"], ["yo"]) # doctest: +SKIP
    ['yo']
    """
    # Hint: You can only compare up to the shortest list's length.
    # Hint: Use a loop that goes through each index and compare len(a[i]) vs len(b[i]).
    # Hint: Remember to break ties by choosing b[i].

#4 Complete the function highest scores which takes in a list of players and their sccores and 
# returns a list of tuples containing the player and their highest score

def highest_scores(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """From a list of (player, score) pairs, return the pairs showing
    the highest score achieved by each player.

    >>> highest_scores([("Luna", 8), ("Kai", 10), ("Luna", 12), ("Kai", 7), ("Taro", 9)]) # doctest: +SKIP
    [('Luna', 12), ('Kai', 10), ('Taro', 9)]
    """
    # Hint: Use a dictionary where each key is a player and each value is their best score so far.
    # Hint: If a player is not in the dictionary yet, add them with their current score.
    # Hint: If they are already there, update only if the new score is higher.
    # Hint: Convert the dictionary back to a list of (player, score) pairs before returning.


#5 Write a recursive function reverse_word that reverses a string without using loops.

def reverse_word(word: str) -> str:
    """Return the reverse of a word using recursion only (no loops).
    
    >>> reverse_word("hello") # doctest: +SKIP
    'olleh'
    >>> reverse_word("z") # doctest: +SKIP
    'z'
    >>> reverse_word("") # doctest: +SKIP
    ''
    """
    # Hint: Base case — what should happen if the string is empty or one character long?
    # Hint: Recursive step — take the last character and add it to the reverse of the rest.
    # Hint: Use slicing like word[:-1] and word[-1] to separate parts of the string.


#Bonus problem 1 Complete function matches.

def matches(x_l: list[str], y_l: list[str]) -> list[bool]:
    """Returns list m in which each m[i] is
    True if and only if x_l[i] is same as y_l[i].
    x_l and y_l are parallel lists.
    >>> matches(["a", "b", "c"], ["a", "x", "c"]) # doctest: +SKIP
    [True, False, True]
    """
    assert len(x_l) == len(y_l), "x_l and y_l must be parallel lists"
    # Hint: Loop over the range of indices and compare x_l[i] to y_l[i].
    # Hint: Append True or False to a new list depending on whether they match.


#Bonus problem 2 Write a recursive function is_palindrome that determines whether a string reads the same backward as forward.

def is_palindrome(word: str) -> bool:
    """Return True if word is a palindrome, False otherwise.
    Ignore case differences.
    
    >>> is_palindrome("racecar") # doctest: +SKIP
    True
    >>> is_palindrome("Python") # doctest: +SKIP
    False
    >>> is_palindrome("") # doctest: +SKIP
    True
    """
    # Hint: Base case — when is a string definitely a palindrome?
    # Hint: Compare the first and last characters.
    # Hint: Recursively check the substring between them.
    # Hint: Convert the string to lowercase first so case doesn’t matter.


#Bonus problem 3 return a list of tuples containing a product name and then it's average price

def average_price(entries: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """From a list of (product, price) pairs, return a list of (product, average)
    tuples giving the average price per product. Round each average to one decimal place.

    >>> average_price([
    ... ("banana", 1.0), ("apple", 2.0), ("banana", 1.5),
    ... ("apple", 3.0), ("pear", 2.2)])                     # doctest: +SKIP
    [('banana', 1.2), ('apple', 2.5), ('pear', 2.2)]
    """
    # Hint: Use a dictionary that maps each product to [total_price, count].
    # Hint: Update the total and count for each entry.
    # Hint: After the loop, compute the average for each product and round it.
    # Hint: Return the results as a list of (product, average) tuples.


#Bonus problem 4 Write a recursive function that computes the sum of all even integers in a list. No loops may be used.

def sum_evens(nums: list[int]) -> int:
    """Return the sum of even numbers in nums using recursion only.
    
    >>> sum_evens([1, 2, 3, 4, 5, 6]) # doctest: +SKIP
    12
    >>> sum_evens([7, 9, 11]) # doctest: +SKIP
    0
    >>> sum_evens([]) # doctest: +SKIP
    0
    """
    # Hint: Base case — what should you return if the list is empty?
    # Hint: Recursive step — check whether the first number is even.
    # Hint: If it’s even, add it to the result of the recursive call on the rest of the list.
    # Hint: Use nums[0] and nums[1:] to separate the first element from the rest.



if __name__ == "__main__":
    import doctest
    doctest.testmod()