def max_list(some_list):
    """
    Ques no.1: Write a Python function to find the Max of three numbers.

    """
    largest = some_list[0]
    for number in some_list:
        if number > largest:
            largest = number

    return largest


def sum_list(some_list):
    """
    Ques no.2: Write a Python function to sum all the numbers in a list.

    """
    sum = 0
    for number in some_list:
        sum += number
    return sum


def mul_list(some_list):
    """
    Ques no.3: Write a Python function to multiply all the numbers in a list.

    """
    mul = 1
    for number in some_list:
        mul *= number
    return mul


def rev_string(some_string):
    """
    Ques no.4: Write a Python program to reverse a string.

    """
    some_string = list(reversed(some_string))
    reversed_string = ''
    for alpha in some_string:
        reversed_string += alpha
    return reversed_string


def factorial(number):
    """
    Ques no.5: Write a Python function to calculate the factorial of 
    a number (a non-negative integer). The function accepts the number as an argument.

    """
    fact = 1
    for num in range(1,number+1):
        fact *= num 
    return fact


def check_range(number, num1, num2):
    """
    Ques no.6: Write a Python function to check whether a number is in a given range.

    """
    if number in range(num1,num2+1):
        print(f"{number} is in range {num1} - {num2}.")
    else:
        print(f"{number} is not in range {num1} - {num2}.")


def count_up_low(some_string):
    """
    Ques no.7: Write a Python function that accepts a string and 
    calculate the number of upper case letters and lower case letters.

    """
    up_count = 0
    low_count = 0
    for alpha in some_string:
        if alpha >= 'A' and alpha <= 'Z':
            up_count += 1
        elif alpha >= 'a' and alpha <= 'z':
            low_count += 1 
    return up_count, low_count


def unique_list(some_list):
    """
    Ques no.8: Write a Python function that takes a list and returns
    a new list with unique elements of the first list.

    """
    return list(set(some_list))


def prime_check(number):
    """
    Ques no.9: Write a Python function that takes a number as a parameter
    and check the number is prime or not.

    """
    count = 0
    for num in range(1, number+1):
        if number % num == 0:
            count += 1

    if count <= 2:
        return "Prime"
    else:
        return "Not Prime"


def even_list(some_list):
    """
    Ques no.10: Write a Python program to print the even numbers from a given list.

    """
    even_list = []
    for number in some_list:
        if number % 2 == 0:
            even_list.append(number)
    
    return even_list


def unknown_mul(number):
    """
    Ques no.12: Write a Python program to create a function that takes 
    one argument, and that argument will be multiplied with 
    an unknown given number.

    """
    return lambda x: x * number
