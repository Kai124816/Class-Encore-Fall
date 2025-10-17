#Solutions to the write your own function problems

#Problem 1
def longest_word(words: list[str]) -> str:
    """Return the longest element of words."""
    longest_word = ""
    iteration = 0
    for word in words:
        iteration += 1
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

#Uncomment print statements to test answers
# print(longest_word(['we', 'know', 'how', 'to', 'select', 'extremes'])) #Should print 'extremes' 
# print(longest_word(['we', 'already', 'know', 'how'])) #Should print 'already' 
# print(longest_word(['really?'])) #Should print 'really?' 

#Problem 2
def count_ge(nums: list[int], min: int) -> int:
    """Returns a count of elements in nums whose value is
    at least (>=) min."""
    count = 0
    for num in nums:
        if num >= min:
            count += 1
    return count

#Uncomment print statements to test answers
# print(count_ge([1, 2, 3, 4, 5], 3)) #Should print 3
# print(count_ge([-10, 17, -3, 5], 0)) #Should print 2
# print(count_ge([7, 12, 17], 99)) #Should print 0

#Problem 3
def sum_even(nums: list[int]) -> int:
    """Return the sum of all even numbers in nums."""
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum

# Uncomment print statements to test answers
# print(sum_even([1, 2, 3, 4, 5, 6])) # Should print 12
# print(sum_even([7, 9, 11])) # Should print 0
# print(sum_even([-2, -4, 3])) # Should print -6

#Problem 4
def word_lengths(words: list[str]) -> dict[str, int]:
    """Return a dictionary mapping each word to its length."""
    word_dict = {}
    for word in words:
        if word not in word_dict:
            word_dict[word] = len(word)
    return word_dict

# Uncomment print statements to test answers
# print(word_lengths(['cat', 'dog'])) # Should print {'cat': 3, 'dog': 3}
# print(word_lengths(['hi', 'there', 'hi'])) # Should print {'hi': 2, 'there': 5}
# print(word_lengths([])) # Should print {}

#Problem 5
def multiply_all(nums: list[int]) -> int:
    """Return the product of all numbers in nums.
    If the list is empty, return 1."""
    mul = 1
    for num in nums:
        mul *= num
    return mul

# Uncomment print statements to test answers
# print(multiply_all([2, 3, 4])) # Should print 24
# print(multiply_all([5])) # Should print 5
# print(multiply_all([])) # Should print 1