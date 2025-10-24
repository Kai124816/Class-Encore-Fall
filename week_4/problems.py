#problem 1
"""
Iterate through a dictionary and sum all of it's values.
"""
def sum_vals(val_dict:dict) -> int:
    "Sum all of the dictionary's values"

# print(sum_vals({'apple': 3, 'banana': 2, 'orange': 1})) #should print 6
# print(sum_vals({'horse': 4, 'pig': 7, 'chicken': 3, 'cat': 2})) #should print 16
# print(sum_vals({})) #should print 0

#problem 2
"""
Iterate through a list and sum all of it's even numbers
"""
def sum_evens(num_list:list[int]) -> int:
    "Sum all of the evens"

# print(sum_evens([1, 2, 3, 4, 5, 6]))  # should print 12
# print(sum_evens([7, 9, 11]))           # should print 0
# print(sum_evens([0, 2, 4, 8]))         # should print 14

#Problem 3
"""
Write a function word_count(sentence) that takes a list of strings and returns a 
dictionary where the keys are words and the values are the number of 
times each word appears.
"""
def word_count(sentence:list[str]) -> dict[str]:
    """Returns a count of each word"""

# print(word_count(["apple", "banana", "apple", "orange", "banana", "apple"]))  
# # should print {'apple': 3, 'banana': 2, 'orange': 1}
# print(word_count(["cat", "dog", "dog", "cat", "cat"]))  
# # should print {'cat': 3, 'dog': 2}
# print(word_count([]))  
# # should print {}

#Problem 4
"""
Write a function common_elements(list1, list2) that takes two lists and returns a 
new list containing only the elements that appear in both.
"""
def common_elements(list1:list[int], list2:list[int]) -> list[int]:
    """return the elements that appear in both"""
    return None

# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # should print [3, 4]
# print(common_elements([1, 1, 2, 3], [1, 3, 5]))     # should print [1, 3]
# print(common_elements([10, 20, 30], [40, 50]))      # should print []

#Problem 5
"""
Write a function most_frequent_word(sentence) that returns the word that appears 
most frequently in a sentence represented by a list of strings. In case of a tie, 
return the word that appears first.
"""
def most_frequent_word(sentence: list[str]) -> str:
    """return the element that appears most frequently"""
    return None
    
# print(most_frequent_word(["cat", "dog", "cat", "bird", "dog", "cat"]))  
# # should print 'cat'
# print(most_frequent_word(["apple", "banana", "banana", "apple"]))  
# # should print 'apple' (tie, 'apple' appears first)
# print(most_frequent_word(["one"]))  
# # should print 'one'

#problem 6
"""
Write a function filter_greater which takes in a list and a threshold and returns a new one containing 
only the elements from the input list that are greater than the threshold.
"""
def filter_greater(li: list[int], threshold: int) -> list[int]:
    """All elements must be greater than a given threshold"""
    return None

#print(filter_greater([1, 5, 10, 15], 7))     # should print [10, 15]
# print(filter_greater([10, 9, 8, 7], 10))     # should print []
# print(filter_greater([], 3))                 # should print []

#problem 7
"""
Write a function filter_greater_keys which takes in a dictionary and a threshold and returns
a list of dictionary keys with values that are greater than or equal to the threshold
"""
def filter_greater_keys(d: dict[str], threshold: int) -> list[str]:
    """All keys must have values greater than a given threshold"""
    return None

# print(filter_greater_keys({'apple': 3, 'banana': 7, 'pear': 10}, 5))  
# should print ['banana', 'pear']
# print(filter_greater_keys({'cat': 1, 'dog': 2}, 3))  
# should print []
# print(filter_greater_keys({}, 0))  
# should print []

#problem 8
"""
Write a function vals_greater_than which takes in a list and a threshold and returns
true if the total sum of list elements is greater than the threshold and returns false if 
the total sum of list elements is less than the threshold
"""
def vals_greater_than(li: list[int], threshold: int) -> bool:
    return None

# print(vals_greater_than([1, 2, 3], 5))     # should print True
# print(vals_greater_than([1, 2, 3], 6))     # should print False
# print(vals_greater_than([], 0))            # should print False

