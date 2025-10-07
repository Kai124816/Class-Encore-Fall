## Write your own function problems

#Problem 1
def count_nums(s:str) -> int:
    """Takes a string and counts 
    the number of digits in the string
    Ex: count_nums("abc1234") -> 4
    """
    digits = "0123456789"
    count = 0
    for char in s:
        if char in digits:
            count += 1

    return count

print(count_nums("hello")) #should print 0
print(count_nums("cs210")) #should print 3
print(count_nums("python3")) #should print 1

#Problem 2
def sum_of_range(a:int, b:int) -> int:
    """Write a function that takes in two numbers a and b
    and returns the sum of all the numbers from a to b (not including b).
    Ex: sum_of_range(3,6) -> 12
    """
    total = 0
    for i in range(a,b):
        total += i

    return total

print(sum_of_range(2,4)) #should print 5
print(sum_of_range(1,1)) #should print 0
print(sum_of_range(8,11)) #should print 27


#Problem 3
def consonants_in_string(s:str) -> int:
    """Takes a string and counts 
    the number of numbers in the string
    Ex: count_nums("abcdefg") -> 5
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char not in vowels:
            count += 1
    return count

print(consonants_in_string("dog")) #should print 2
print(consonants_in_string("class encore")) #should print 8
print(consonants_in_string("aeiou")) #should print 0


#Problem 4
def middle(a:int, b:int, c:int) -> int:
    """ Write a function that takes in three different integers and 
    returns the integer with the intermediate value IE the value in the middle.
    Ex: middle(4,12,7)->7
    """
    if a >= b and a >= c:
        if b >= c:
            return c
        else:
            return b
    elif b >= c:
        if c >= a:
            return a
        return b
    else:
        if a >= b:
            return a
        else:
            return b

print(middle(1,2,3)) #should print 2
print(middle(1,1,3)) #should print 1
print(middle(4,8,11)) #should print 8
