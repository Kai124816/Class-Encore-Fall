#What does this print problems

#Problem 1
def good_sum(li: list[int]) -> int:
    """Just the good ones."""
    result = 0
    for el in li:
        if el >= 10:
            result += el
    return result
# print(good_sum([-5, 10, 35, 10, -10])) #Uncomment to test answer

#Problem 2
def sum_of_lengths(li: list[str]) -> int:
    sum = 0
    for str in li:
        if len(str) % 2 == 0:
            sum += len(str)
    return sum
# print(sum_of_lengths(["hello", "CS", "Python", "good", "string"])) #Uncomment to test answer

#Problem 3
def name_count(names: list[str]) -> dict:
    count = {}
    for n in names:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1
    return count
# print(name_count(["Ada", "Bob", "Ada"])) #Uncomment to test answer

#Problem 4
def sum_matrix(mat: list[list[int]]) -> int:
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if (i + j) % 2 == 0:
                sum += mat[i][j]
    return sum
# print(sum_matrix([[1, 2], [3, 4]])) #Uncomment to test answer

#Problem 5
CATS = ["tiger", "lion", "cougar", "leopard"]
ANIMALS = ["horse", "cougar", "dog", "tiger"]
def is_feline(animal: str) -> bool:
    """Does it purr? Does it have sharp teeth?"""
    for cat in CATS:
        if animal == cat:
            return True
    return False

def pet_chooser(choices: list[str]) -> list[str]:
    """Which animals would make good pets?"""
    selection = []
    for choice in choices:
        if is_feline(choice):
            selection.append(choice)
    return selection
#print(pet_chooser(ANIMALS)) #Uncomment to test answer


#Write your own function problems

#Problem 1
def longest_word(words: list[str]) -> str:
    """Return the longest element of words."""
    return ""

#Uncomment print statements to test answers
#print(longest_word(['we', 'know', 'how', 'to', 'select', 'extremes'])) #Should print 'extremes' 
#print(longest_word(['we', 'already', 'know', 'how'])) #Should print 'already' 
#print(longest_word(['really?'])) #Should print 'really' 

#Problem 2
def count_ge(nums: list[int], min: int) -> int:
    """Returns a count of elements in nums whose value is
    at least (>=) min."""
    return 0 

#Uncomment print statements to test answers
# print(count_ge([1, 2, 3, 4, 5], 3)) #Should print 3
# print(count_ge([-10, 17, -3, 5], 0)) #Should print 2
# print(count_ge([7, 12, 17], 99)) #Should print 0

#Problem 3
def sum_even(nums: list[int]) -> int:
    """Return the sum of all even numbers in nums."""
    return 0

# Uncomment print statements to test answers
# print(sum_even([1, 2, 3, 4, 5, 6])) # Should print 12
# print(sum_even([7, 9, 11])) # Should print 0
# print(sum_even([-2, -4, 3])) # Should print -6

#Problem 4
def word_lengths(words: list[str]) -> dict[str, int]:
    """Return a dictionary mapping each word to its length."""
    return {}

# Uncomment print statements to test answers
# print(word_lengths(['cat', 'dog'])) # Should print {'cat': 3, 'dog': 3}
# print(word_lengths(['hi', 'there', 'hi'])) # Should print {'hi': 2, 'there': 5}
# print(word_lengths([])) # Should print {}

#Problem 5
def multiply_all(nums: list[int]) -> int:
    """Return the product of all numbers in nums.
    If the list is empty, return 1."""
    return 0

# Uncomment print statements to test answers
# print(multiply_all([2, 3, 4])) # Should print 24
# print(multiply_all([5])) # Should print 5
# print(multiply_all([])) # Should print 1






