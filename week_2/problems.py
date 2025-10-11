## What does this print problems

#Problem 1
def mystery(n):
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            total += i
        elif i % 2 == 0:
            total -= i
        else:
            total += 1
    return total

# print(mystery(6)) #what will this print

#Problem 2
def mystery2(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total -= i * 2
        else:
            total += i
    return total

# print(mystery2(5)) #what will this print

#Problem 3
def mystery3(s):
    count = 0
    vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
    for ch in s:
        if ch in vowel_list:
            count += 2
        elif ch.isalpha():
            count += 1
    return count

# print(mystery3("Hello!")) #what will this print

#Problem 4
def mystery4(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            if i % 4 == 0:
                total += i
            else:
                total -= i
        else:
            total += 2
    return total

# print(mystery4(4)) #what will this print

#Problem 5
def mystery5(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()
    return result

# print(mystery5("python")) #what will this print

#Problem 6
def mystery6(n):
    total = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            total += i
    return total

# print(mystery6(10)) #what will this print


## Write your own function problems

#Problem 1
def count_nums(s:str) -> int:
    """Takes a string and counts 
    the number of numbers in the string
    Ex: count_nums("abc1234") -> 4
    """

# print(count_nums("hello")) #should print 0
# print(count_nums("cs210")) #should print 3
# print(count_nums("python3")) #should print 1

#Problem 2
def sum_of_range(a:int, b:int) -> int:
    """Write a function that takes in two numbers a and b
    and returns the sum of all the numbers from a to b (not including b).
    Ex: sum_of_range(3,6) -> 12
    """

# print(sum_of_range(2,4)) #should print 5
# print(sum_of_range(1,1)) #should print 0
# print(sum_of_range(8,11)) #should print 27


#Problem 3
def consonants_in_string(s:str) -> int:
    """Takes a string and counts 
    the number of numbers in the string
    Ex: count_nums("abcdefg") -> 5
    """
    return

# print(consonants_in_string("dog")) #should print 2
# print(consonants_in_string("class encore")) #should print 7
# print(consonants_in_string("aeiou")) #should print 1


#Problem 4
def middle(a:int, b:int, c:int) -> int:
    """ Write a function that takes in three different integers and 
    returns the integer with the intermediate value IE the value in the middle.
    Ex: middle(4,12,7)->7
    """
    return

# print(middle(1,2,3)) #should print 2
# print(middle(1,1,3)) #should print 1
# print(middle(4,8,11)) #should print 8


