#problem 1
"""
Iterate through a dictionary and sum all of its values.
"""
def sum_vals(val_dict:dict) -> int:
    "Sum all of the dictionary's values"
    # Start a running total at 0
    total = 0
    
    # Loop through each key in the dictionary
    for el in val_dict:
        # Add the value associated with that key to the total
        total += val_dict[el]
    
    # Return the sum of all values
    return total

# print(sum_vals({'apple': 3, 'banana': 2, 'orange': 1})) #should print 6
# print(sum_vals({'horse': 4, 'pig': 7, 'chicken': 3, 'cat': 2})) #should print 16
# print(sum_vals({})) #should print 0


#problem 2
"""
Iterate through a list and sum all of its even numbers
"""
def sum_evens(num_list:list[int]) -> int:
    "Sum all of the evens"
    # Initialize total to 0
    total = 0
    
    # Loop through every number in the list
    for num in num_list:
        # Check if the number is even (divisible by 2)
        if num % 2 == 0:
            # Add the even number to the total
            total += num
    
    # Return the total of all even numbers
    return total

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
    # Create an empty dictionary to store word counts
    count_dict = {}
    
    # Loop through each word in the list
    for word in sentence:
        # If the word is not in the dictionary yet, add it with count 1
        if word not in count_dict:
            count_dict[word] = 1
        # Otherwise, increment the existing count
        else:
            count_dict[word] += 1
    
    # Return the dictionary containing word frequencies
    return count_dict

# print(word_count(["apple", "banana", "apple", "orange", "banana", "apple"]))  
# should print {'apple': 3, 'banana': 2, 'orange': 1}
# print(word_count(["cat", "dog", "dog", "cat", "cat"]))  
# should print {'cat': 3, 'dog': 2}
# print(word_count([]))  
# should print {}

#Problem 4
"""
Write a function common_elements(list1, list2) that takes two lists and returns a 
new list containing only the elements that appear in both.
"""
def common_elements(list1:list[int], list2:list[int]) -> list[int]:
    """Return the elements that appear in both"""
    # Create an empty list to store shared elements
    common = []
    
    # Loop through every element in the first list
    for el in list1:
        # Check two things:
        # (1) if the element also appears in the second list
        # (2) and if it's not already in the 'common' list (avoid duplicates)
        if el in list2 and el not in common:
            common.append(el)
    
    # Return the list of shared elements
    return common

# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # should print [3, 4]
# print(common_elements([1, 1, 2, 3], [1, 3, 5]))     # should print [1, 3]
# print(common_elements([10, 20, 30], [40, 50]))      # should print []


#Problem 5
"""
Write a function most_frequent_word(sentence) that returns the word that appears 
most frequently in a sentence represented by a list of strings. In case of a tie, 
return the word that appears first. If the list is empty return an empty string.
"""
def most_frequent_word(sentence: list[str]) -> str:
    """Return the element that appears most frequently"""
    # Handle the edge case of an empty list
    if len(sentence) == 0:
        return ""
    
    # Create a dictionary to count occurrences of each word
    count_dict = {}
    for word in sentence:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    
    # Track the word that appears most frequently
    most_frequent = ""
    # Initialize its count to 0 so any real word will replace it
    count_dict[most_frequent] = 0
    
    # Loop through the dictionary and find the word with the highest count
    for word in count_dict:
        # If this word's count is higher than the current max, update it
        if count_dict[word] > count_dict[most_frequent]:
            most_frequent = word
    
    # Return the most frequent word found
    return most_frequent

# print(most_frequent_word(["cat", "dog", "cat", "bird", "dog", "cat"]))  
# should print 'cat'
# print(most_frequent_word(["apple", "banana", "banana", "apple"]))  
# should print 'apple' (tie, 'apple' appears first)
# print(most_frequent_word(["one"]))  
# should print 'one'


#problem 6
"""
Write a function filter_greater which takes in a list and a threshold and returns a new one containing 
only the elements from the input list that are greater than the threshold.
"""
def filter_greater(li: list[int], threshold: int) -> list[int]:
    """All elements must be greater than a given threshold"""
    # Create a new list to hold numbers greater than the threshold
    greater_than = []
    
    # Loop through all numbers in the list
    for el in li:
        # Add the number to the new list if it passes the test
        if el > threshold:
            greater_than.append(el)
    
    # Return the filtered list
    return greater_than

# print(most_frequent_word(["cat", "dog", "cat", "bird", "dog", "cat"]))  
# should print 'cat'
# print(most_frequent_word(["apple", "banana", "banana", "apple"]))  
# should print 'apple' (tie, 'apple' appears first)
# print(most_frequent_word(["one"]))  
# should print 'one'



#problem 7
"""
Write a function filter_greater_keys which takes in a dictionary and a threshold and returns
a list of dictionary keys with values that are greater than or equal to the threshold.
"""
def filter_greater_keys(d: dict[str], threshold: int) -> list[str]:
    """All keys must have values greater than a given threshold"""
    # Create an empty list to hold keys that pass the check
    greater_than = []
    
    # Loop through each key in the dictionary
    for el in d:
        # If the value associated with that key is greater than the threshold
        if d[el] >= threshold:
            # Add the key to the results list
            greater_than.append(el)
    
    # Return the list of keys with large enough values
    return greater_than

# print(filter_greater_keys({'apple': 3, 'banana': 7, 'pear': 10}, 5))  
# should print ['banana', 'pear']
# print(filter_greater_keys({'cat': 1, 'dog': 2}, 3))  
# should print []
# print(filter_greater_keys({}, 0))  
# should print []


#problem 8
"""
Write a function vals_greater_than which takes in a list and a threshold and returns
True if the total sum of list elements is greater than the threshold, and False otherwise.
"""
def vals_greater_than(li: list[int], threshold: int) -> bool:
    # Start a running total at 0
    total = 0
    
    # Add up all numbers in the list
    for el in li:
        total += el
    
    # Compare the total to the threshold
    if total > threshold:
        return True
    # If it's not greater, return False
    return False

# print(vals_greater_than([1, 2, 3], 5))     # should print True
# print(vals_greater_than([1, 2, 3], 6))     # should print False
# print(vals_greater_than([], 0))            # should print False

