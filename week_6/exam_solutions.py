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
    
    >>> shorter_first(["bear", "cat", "alligator"], ["dog", "elephant", "ant"]) 
    ['dog', 'cat', 'ant']
    >>> shorter_first(["hi", "there"], ["yo"]) 
    ['yo']
    """
    shortest = []
    max_index = 0
    if(len(a) < len(b)):
        max_index = len(a)
    else:
        max_index = len(b)

    for i in range(max_index):
        if len(a[i]) < len(b[i]):
            shortest.append(a[i])
        else:
            shortest.append(b[i])
    
    return shortest

#4 Complete the function highest scores which takes in a list of players and their sccores and 
# returns a list of tuples containing the player and their highest score

def highest_scores(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """From a list of (player, score) pairs, return the pairs showing
    the highest score achieved by each player.

    >>> highest_scores([("Luna", 8), ("Kai", 10), ("Luna", 12), ("Kai", 7), ("Taro", 9)]) 
    [('Luna', 12), ('Kai', 10), ('Taro', 9)]
    """
    score_dict = {}
    for player,score in records:
        if player in score_dict and score > score_dict[player]:
            score_dict[player] = score
        elif player not in score_dict:
            score_dict[player] = score
    
    hs_list = []
    for player,score in score_dict.items():
        hs_list.append((player,score))
    
    return hs_list


#5 Write a recursive function reverse_word that reverses a string without using loops.
#Hint: You can use the plus operator to concatanate strings 
#Hint: list[:-1] can be used to represent a list with all of the elements besides the last one
# for example: if list = "world", list[:-1] = "worl"

def reverse_word(word: str) -> str:
    """Return the reverse of a word using recursion only (no loops).
    
    >>> reverse_word("hello") 
    'olleh'
    >>> reverse_word("z") 
    'z'
    >>> reverse_word("") 
    ''
    """
    if len(word) <= 1:
        return word
    else:
        return word[-1] + reverse_word(word[:-1])

#Bonus problem 1 Complete function matches.

def matches(x_l: list[str], y_l: list[str]) -> list[bool]:
    """Returns list m in which each m[i] is
    True if and only if x_l[i] is same as y_l[i].
    x_l and y_l are parallel lists.
    >>> matches(["a", "b", "c"], ["a", "x", "c"])
    [True, False, True]
    """
    assert len(x_l) == len(y_l), "x_l and y_l must be parallel lists"

    match_list = []
    for i in range(len(x_l)):
        if x_l[i] == y_l[i]:
            match_list.append(True)
        else:
            match_list.append(False)
    
    return match_list


#Bonus problem 2 Write a recursive function is_palindrome that determines whether a string reads the same backward as forward.

def is_palindrome(word: str) -> bool:
    """Return True if word is a palindrome, False otherwise.
    Ignore case differences.
    
    >>> is_palindrome("racecar") 
    True
    >>> is_palindrome("Python") 
    False
    >>> is_palindrome("") 
    True
    """
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])


#Bonus problem 3 return a list of tuples containing a product name and then it's average price

def average_price(entries: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """From a list of (product, price) pairs, return a list of (product, average)
    tuples giving the average price per product. Round each average to one decimal place.

    >>> average_price([
    ... ("banana", 1.0), ("apple", 2.0), ("banana", 1.5),
    ... ("apple", 3.0), ("pear", 2.2)])                     
    [('banana', 1.2), ('apple', 2.5), ('pear', 2.2)]
    """
    price_dict = {}
    for food, price in entries:
        if food not in price_dict:
            price_dict[food] = [price, 1]
        else:
            price_dict[food][0] += price
            price_dict[food][1] += 1

    ap_list = []
    for food, (total_price, total_items) in price_dict.items():
        ap = round(total_price / total_items, 1)
        ap_list.append((food, ap))
    
    return ap_list


#Bonus problem 4 Write a recursive function that computes the sum of all even integers in a list. No loops may be used.

def sum_evens(nums: list[int]) -> int:
    """Return the sum of even numbers in nums using recursion only.
    
    >>> sum_evens([1, 2, 3, 4, 5, 6]) 
    12
    >>> sum_evens([7, 9, 11]) 
    0
    >>> sum_evens([]) 
    0
    """
    if len(nums) == 0:
        return 0
    elif nums[0] % 2 != 0:
        return 0 + sum_evens(nums[1:])
    else:
        return nums[0] + sum_evens(nums[1:])

if __name__ == "__main__":
    import doctest
    doctest.testmod()