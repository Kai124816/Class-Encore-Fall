#Problem 1
"""
Write a function multiple_appearances(l1:list[int]) that takes in a list of 
integers and returns a list of integers that appear more than once.
"""
def multiple_appearances(l1:list[int]) -> list[int]:
    "Which numbers appear more than once"
    pass

# print(multiple_appearances([1,2,2,3,3,4,4,4])) #should print [2,3,4]
# print(multiple_appearances([6,6,6,8,8,8])) #should print [6,8]
# print(multiple_appearances([1,2,3,4,5])) #should print []

#Problem 2
"""
Write a function merge_dicts(d1, d2) that merges two dictionaries. If a key appears in both, 
its value in the result should be the sum of the two values.
"""
def merge_dicts(d1:dict, d2:dict) -> dict:
    "Merge the two dictionaries"
    pass

# print(merge_dicts({'a': 3, 'b': 2}, {'b': 5, 'c': 10})) #should print {'a': 3, 'b': 7, 'c': 10}
# print(merge_dicts({'car': 2, 'plane': 3, 'bike': 5},{'car': 0, 'plane': 2, 'horse': 1})) #should print {'car': 2, 'plane': 5, 'bike': 5, 'horse': 1}
# print(merge_dicts({},{})) #should print {}

#Problem 3
"""
Write a function invert_dict(d) that takes a dictionary and returns a new one where 
each value becomes a key mapping to a list of keys that had that value.
"""
def invert_dict(d1:dict) -> dict:
    "Invert the dictionary"
    pass

# print(invert_dict({'a': 1, 'b': 2, 'c': 1})) #should print {1: ['a', 'c'], 2: ['b']}
# print(invert_dict({'cat': 3, 'dog': 2})) #should print {3: ['cat'], 2: ['dog']}
# print(invert_dict({'house': 2})) #should print {2: ['house']}

#Problem 4
"""
Write a function second_greatest(l1:list[int]) that takes in a list of integers
and returns the second largest number in the list. You may assume the list has
at least two distinct elements.
"""
def second_greatest(l1:list[int]) -> int:
    "Returns the second greatest element in the list"

# print(second_greatest([1,2,3,4,5])) #should print 4
# print(second_greatest([10,10,9,8,8,7])) #should print 9
# print(second_greatest([100,50])) #should print 50


#Problem 5
"""
Write a function sum_second_half(l1:list[int]) that takes in a list of integers 
and returns the sum of the elements in the second half of the list. If the list 
has an odd length, the middle element should be considered part of the second half.
"""
def sum_second_half(l1:list[int]) -> int:
    "Sum the second half of the list"
    pass

# print(sum_second_half([1,2,3,4])) #should print 7 (3+4)
# print(sum_second_half([1,2,3,4,5])) #should print 12 (3+4+5)
# print(sum_second_half([10])) #should print 10


#Problem 6
"""
Write a function fib(num:int) that returns the nth number in the Fibonacci 
sequence recursively. The Fibonacci sequence starts with 0 and 1, and each 
number afterward is the sum of the two before it.
"""
def fib(num:int) -> int:
    "Return the nth number in the fibonacci sequence recursively"
    pass

# print(fib(0)) #should print 0
# print(fib(1)) #should print 1
# print(fib(6)) #should print 8

#Problem 7
"""
Write a function factorial(n:int) that recursively computes 
the factorial of a number
"""
def factorial(n: int) -> int:
    "Compute the factorial of a number."
    pass
    
# print(factorial(4)) #should print 24
# print(factorial(5)) #should print 120
# print(factorial(6)) #should print 720


#Problem 8
"""
Write a function sum_of_digits(n:int) that recursively
computes the sum of a number's digits
"""
def sum_of_digits(num: int) -> int:
    "Compute the sum of all the digits in a number."
    pass

# print(sum_of_digits(423)) #should print 9
# print(sum_of_digits(52)) #should print 7
# print(sum_of_digits(1238)) #should print 14
# print(sum_of_digits(12500)) 
