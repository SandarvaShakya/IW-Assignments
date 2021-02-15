from DataTypes import Questions
from Functions import Questions_func
from functools import reduce

while True:
    print("""
Choose Section:
    1. Datatypes
    2. Functions
    3. Exit
""")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("Question number 1 - 46")
        while True:
            check = input("Do you want to enter question number(Y/N): ")
            if check == 'n' or check == 'N':
                break
            else:
                try:
                    option = int(input("Choose Question Number: "))
                except ValueError:
                    print("Ouestion number must be an interger!!")
                    continue
                try:
                    print(f"\nQuestion number {option}: ")
                    func = Questions.functions[option]
                    func()
                # except TypeError:
                #     print("Enter number!!")
                except KeyError:
                    print("Question number does not exist!!")
    elif option == 2:
        print("Question number 1 - 20")
        while True:
            check = input("Do you want to enter question number(Y/N): ")
            if check == 'n' or check == 'N':
                break
            else:
                try:
                    option = int(input("Choose Question Number: "))
                except ValueError:
                    print("Ouestion number must be an interger!!")
                    continue
                print(f"\nQuestion number {option}: ")
                if option == 1:
                    some_numbers = [4, 5, 7]
                    result = Questions_func.max_list(some_numbers)
                    print(f"Numbers = {some_numbers}")
                    print(f"The largest number is: {result}")    
                elif option == 2:
                    some_list = [1, 2, 3, 4, 5]
                    result = Questions_func.sum_list(some_list)
                    print(f"Numbers = {some_list}")
                    print(f"The sum is: {result}") 
                elif option == 3:
                    some_list = [1, 2, 3, -4, 5]
                    result = Questions_func.mul_list(some_list)
                    print(f"Numbers = {some_list}")
                    print(f"The multiplication is: {result}") 
                elif option == 4:
                    some_string = "1234abcd"
                    result = Questions_func.rev_string(some_string)
                    print("Original string: ", some_string)
                    print("Reversed string: ", result)
                elif option == 5:
                    number = int(input("Enter a number: "))
                    result = Questions_func.factorial(number)
                    print(f"The factorial of {number} is: ", result)
                elif option == 6:
                    Questions_func.check_range(3, 4, 10)
                    Questions_func.check_range(3, 3, 10)
                elif option == 7:
                    some_string = input("Enter a string: ")
                    result = Questions_func.count_up_low(some_string)
                    print(f"Upper Count = {result[0]}\nLower Count = {result[1]}")
                elif option == 8:
                    some_list = [1,2,3,3,3,3,4,5]
                    print("Original List: ", some_list)
                    result = Questions_func.unique_list(some_list)
                    print("unique list: ", result)
                elif option == 9:
                    number = int(input("Enter a number: "))
                    result = Questions_func.prime_check(number)
                    print(result)
                elif option == 10:
                    some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    print("Original List: ", some_list)
                    result = Questions_func.even_list(some_list)
                    print("Even List: ", result)
                elif option == 11:
                    #lambda function to add 15 to given number
                    number = int(input("Enter number: "))
                    result = lambda x : x + 15
                    print("Result of adding = ", result(number))
                    #lambda function to multiply two number
                    result = lambda x, y : x * y
                    print("Result of multiplication = ",result(2,3))
                elif option == 12:
                    number = int(input("Enter number: "))
                    result = Questions_func.unknown_mul(number)
                    print("Multiplying with 3 = ", result(3))
                elif option == 13:
                    #To sort tuple using lambda function
                    some_tuple = (2, 7, 9, 1)
                    result = lambda x : sorted(x)
                    print("Tuple = ", some_tuple)
                    print("Sorted tuple = ", tuple(result(some_tuple)))
                elif option == 14:
                    #To sort list of dictionary using lambda function
                    some_dict_list = [{1: 1, 2: 4, 3: 9},{1: 2, 2: 5, 3: 2},{1: 10, 2: 20, 3: 30}]
                    print("original: ",some_dict_list)
                    result = sorted(some_dict_list, key = lambda x: x[3])
                    print("Sorted by key 3: ", result)
                elif option == 15:
                    #To filter list with lambda function(even filter)
                    some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    result = list(filter(lambda x: x % 2 == 0, some_list))
                    print("Original List: ",some_list)
                    print("Filtered list = ",result)
                elif option == 16:
                    #To find square and cube of numbers in list using lambda function
                    some_list = [1, 2, 3, 4]
                    result = list(map(lambda x : pow(x, 2), some_list))
                    result1 = list(map(lambda x : pow(x, 3), some_list))
                    print("Original list: ",some_list)
                    print("Squared list: ", result)
                    print("Cubed list: ", result1)
                elif option == 17:
                    #To find if the typed character is the first alphabet
                    some_string = "Hello World"
                    char = input("Enter a character: ")
                    result = lambda x: x == some_string[0]
                    print("Given String: ", some_string)
                    print(result(char))
                elif option == 18:
                    #To find if given string is number or not
                    some_string = input("Enter string: ")
                    result = lambda x : x.isdigit()
                    print(result(some_string))
                elif option == 19:
                    #To Create Fibonacci series upto n using lambda
                    result = lambda x: reduce(lambda y, _: y + [y[-1] + y[-2]], range(x - 2), [0,1])
                    print(result(8))
                elif option == 20:
                    #To find intersection in array
                    list1 = [1, 2, 3, 4, 5]
                    list2 = [3, 4, 5, 6, 7]
                    result = list(filter(lambda x: x in list1, list2))
                    print("List 1: ",list1)
                    print("List 2: ",list2)
                    print("Intersection: ", result)
                else:
                    print("Question number does not exist.")
    elif option == 3:
        exit()
    else:
        print("Invalid Option!")