# Data-Types Questions

def character_frequency():
    """
    Ques no. 1: Write a Python program to count the number of characters
    (character frequency).

    """

    # Code
    dictionary = {}
    some_string = "google.com"
    for alphabet in some_string:
        keys = dictionary.keys()
        if alphabet in keys:
            dictionary[alphabet] += 1
        else:
            dictionary[alphabet] = 1

    sorted_list = sorted(dictionary.items(), reverse=True)
    sorted_list.sort(key= lambda x:x[1], reverse=True)
    sorted_dictionary = dict(sorted_list)
    print(sorted_dictionary)


def manipulate_string():
    """
    Ques no.2: Write a Python program to get a string made of the first
    two and last two chars froam a given string.If the string is less than 2,
    return instead of empty string.

    """

    # Code
    some_string = input("Enter a string: ")
    manipulated_string = some_string[:2] + some_string[-2:]
    print(manipulated_string)


def change_repeated():
    """
    Ques no.3: Write a Python program to get a string from a given 
    string where all occurrences of its first char have been changed to '$',
    except the first char itself.
    
    """

    #Code
    some_string = "restart"
    first_character = some_string[0]
    some_string = some_string.replace(first_character,"$")
    some_string = first_character + some_string[1:]
    
    print(f"Replaced string: {some_string}")


def swap_string():
    """
    Ques no.4: Write a Python program to get a single string from two given
    strings, separated by a space and swap the first two characters of each
    string.

    """

    #Code
    some_string = 'abc','xyz'
    some_string = some_string[1] + ' ' + some_string[0]

    print(some_string)


def ing_adder():
    """
    Ques no.5: Write a Python program to add 'ing' at the end of a given 
    string (length should be at least 3). If the given string already 
    ends with 'ing' then add 'ly' instead. If the string length of the 
    given string is less than 3, leave it unchanged.

    """

    #Code
    some_string = input("Enter a word: ")
    length_string = len(some_string)
    ing_check = some_string[-3:]
    if length_string < 3:
        print(f"Required Output: {some_string}")
    elif ing_check == "ing":
        ly_added_string = some_string[:length_string] + "ly"
        print(f"Required Output: {ly_added_string}")
    else:
        ing_added_string = some_string[:length_string] + "ing"
        print(f"Required Output: {ing_added_string}")


def not_poor():
    """
    Ques no.6: Write a Python program to find the first appearance of the 
    substring 'not' and 'poor' from a given string, if 'not' follows the 
    'poor', replace the whole 'not'...'poor' substring with 'good'. 
    Return the resulting string.

    """

    #Code
    some_string = input("Enter a string: ")
    split_string = some_string.split(" ")
    final_string = ""

    for word in split_string:
        if word == "not":
            index = split_string.index(word)
            for word in split_string[index:]:
                if word == "poor":
                    split_string = split_string[:index]
                    split_string.append("good")
                    for list_word in split_string:
                         final_string += list_word + " "

    if final_string == "":
        final_string = some_string

    print(final_string)


def longest_string():
    """
    Ques no.7: Write a Python function that takes a list of 
    words and returns the length of the longest one.

    """

    #Code
    string_list = []
    number_of_items = int(input("Enter number of strings: "))
    count = 0
    while True:
        if count == number_of_items:
            break
        user_list = input("Enter string: ")
        count += 1
        string_list.append(user_list)

    longest = string_list[0]
    for word in string_list:
        if len(word) > len(longest):
            longest = word
    
    print(f"The longest string is {longest} and its length is {len(longest)}.")


def remove_char():
    """
    Ques no.8:  Write a Python program to remove the n th index character from a nonempty
                string.

    """

    #Code
    some_string = input("Enter a string: ")
    pop_char = int(input("Enter nth character to delete: "))

    some_string = some_string[:pop_char] + some_string[pop_char+1:]
    print(some_string)


def exchange():
    """
    Ques no.9:  Write a Python program to change a given string to a new string where the first
                and last chars have been exchanged.

    """

    #Code
    some_string = input("Enter a string: ")

    resulting_string = some_string[-1] + some_string[1:len(some_string)-1] + some_string[0]

    print(f"Required Output: {resulting_string}")


def remove_odd_index():
    """
    Ques no.10: Write a Python program to remove the characters which have odd index
                values of a given string.

    """

    #Code
    resulting_string = ""
    some_string = input("Enter a string: ")
    for index in range(len(some_string)):
        if index % 2 == 0:
            resulting_string += some_string[index]
    
    print(resulting_string)


def word_count():
    """
    Ques no.11: Write a Python program to count the occurrences of each word in a given
    sentence.

    """

    #Code
    dictionary = {}
    some_string = input("Enter a string: ")

    splitted_string = some_string.split(' ')
    for word in splitted_string:
        keys = dictionary.keys()
        if word in keys:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    print(dictionary)


def change_to_uppper_and_lower():
    """
    Ques no.12: Write a Python script that takes input from the user and displays that input
    back in upper and lower cases.

    """

    #Code
    some_string = input("Enter a string: ")
    print(f"Changing to upper: {some_string.upper()}\nChanging to lower: {some_string.lower()}")


def unique_words_sorted():
    """
    Ques no.13: Write a Python program that accepts a comma separated 
    sequence of words as input and prints the unique words in sorted 
    form (alphanumerically).

    """

    #Code
    final_string = ""
    some_string = input("Enter comma seperated list: ")
    splitted_list = some_string.split(',')
    sorted_set = sorted(set(splitted_list))
    final_string = ",".join(sorted_set)

    print(f"Sorted alphanumerically: {final_string}")


def add_tags():
    """
    Ques no.14: Write a Python function to create the HTML string with tags 
    around the word(s).

    """

    #Code
    tag = input("Enter tag: ")
    content = input("Enter content: ")
    print(f"Output: <{tag}>{content}</{tag}>")


def insert_string_in_middle():
    """
    Ques no.15: Write a Python function to insert a string in the middle of 
    a string.
    
    """

    #Code
    string_in_insert = input('Enter the string inside which to be inserted: ')
    string_to_insert = input("Enter the string to be inserted: ")

    length_of_string_in_insert = len(string_in_insert)//2
    print(f"Final Output: {string_in_insert[:length_of_string_in_insert]}{string_to_insert}{string_in_insert[length_of_string_in_insert:]}")


def sum_of_list():
    """
    Ques no.16: Write a Python program to sum all the items in a list.

    """

    #Code
    some_list = list(input("Enter a list: "))
    sum = 0
    for number in some_list:
        sum += int(number)
    
    print(f"The sum of the list is =  {sum}")


def multiplication_of_list():
    """
    Ques no.17: Write a Python program to multiplyall the items in a list.

    """

    #Code
    some_list = list(input("Enter a list: "))
    product = 1
    for number in some_list:
        product *= int(number)
    
    print(f"The product of list is = {product}")


def largest_in_list():
    """
    Ques no.18: Write a Python program to get the largest number from a list.

    """

    #Code
    some_list = list(input("Enter a list: "))
    largest_number = int(some_list[0])
    for number in some_list:
        if int(number) > largest_number:
            largest_number = int(number)
    
    print(f"The largest number in list is: {largest_number}")


def smallest_in_list():
    """
    Ques no.19: Write a Python program to get the smallest number from a list.

    """

    #Code
    some_list = list(input("Enter a list: "))
    smallest_number = int(some_list[0])
    for number in some_list:
        if int(number) < smallest_number:
            smallest_number = int(number)
    
    print(f"The smallest number in list is: {smallest_number}")


def string_with_same_letters():
    """
    Ques no .20: Write a Python program to count the number of strings where the string
    length is 2 or more and the first and last character are same from a given list of
    strings.

    """

    #Code
    string_count = 0
    some_list = input("Enter a list of string seperated with space: ")
    some_list = some_list.split(' ')
    print(some_list)
    for string in some_list:
        if string[0] == string[-1]:
            string_count += 1
    print(f"The number of string with first and last alphabet same is = {string_count}")


def sorted_tuple_list():
    """
    Ques no.21: Write a Python program to get a list, sorted in increasing order by the last
    element in each tuple from a given list of non-empty tuples.

    """

    #Code
    list_of_tuple = [(2,5,1),(7,5,2),(4,8,3),(1,1,4),(0,6,5),(9,7,6),(8,9,7)]
    list_of_tuple.sort(key= lambda x: x[-1])
       
    print(list_of_tuple)


def remove_duplicates():
    """
    Ques no.22: Write a Python program to remove duplicates from a list.

    """

    #Code
    some_list = input("Enter a list: ")
    some_list = some_list.split(' ')
    remove_dupli = set(some_list)
    some_list = list(remove_dupli)
    some_list.sort()

    print(some_list)


def empty_list_check():
    """
    Ques no.23: Write a Python program to check a list is empty or not.

    """

    #Code
    some_list = input("Enter a list: ")

    check = bool(some_list)
    print(some_list)
    if check == True:  
        print("The list is not empty.")
    else:
        print("The list is empty.")


def clone_list():
    """
    Ques no.24: Write a Python program to clone or copy a list.

    """

    #Code
    some_list = input("Enter a list: ")
    some_list = list(some_list.split(' '))
    cloned_list = []

    for something in some_list:
        cloned_list.append(something)

    print(f"Original list: {some_list}")
    print(f"Cloned list: {cloned_list}")


def check_empty_list_of_dict():
    """
    Ques no.25: Write a Python program to check whether all dictionaries in a 
    list are empty or not.

    """

    #Code
    list_of_dict = [{},{},{},{}]
    empty_count = 0
    for dictionary in list_of_dict:
        if bool(dictionary) == False:
            empty_count += 1

    print(list_of_dict)
    if empty_count == len(list_of_dict):
        print("True")
    else:
        print("False")


def insert_string_in_start():
    """
    Ques no.26: Write a Python program to insert a given string at the beginning 
    of all items in a list.

    """
    #Code
    some_list = input("Enter a list seperated with space: ")
    some_list = list(some_list.split(' '))
    some_string = input("Enter a string to insert: ")
    final_list = []
    for something in some_list:
        something = some_string + str(something)
        final_list.append(something)

    print(f"Original list: {some_list}")
    print(f"String Added List: {final_list}")


def adding_list():
    """
    Ques no.27: Write a Python program to replace the last element in a list with another list.

    """

    #Code
    first_list = [1, 3, 5, 7, 9, 10]
    second_list = [2, 4, 6, 8]
    print(f"First list: {first_list}")
    print(f"Second list: {second_list}")
    first_list.pop()
    for something in second_list:
        first_list.append(something)

    print(f"Resulting list: {first_list}")


def update_dict():
    """
    Ques no.28: Write a Python script to add a key to a dictionary.

    """

    #Code
    dictionary = {0: 10, 1: 20}

    key = input("Enter key to add: ")
    value = input("Enter its value: ")
    to_update = {key: value}

    print(f"Original Dictionary = {dictionary}")
    dictionary.update(to_update)
    print(f"Updated Dictionary = {dictionary}")

    
def concatenate_dicts():
    """
    Ques no.29: Write a Python script to concatenate following dictionaries to create a new
    one.

    """

    #Code
    dictionary1 = {1: 10, 2: 20}
    dictionary2 = {3: 30, 4: 40}
    dictionary3 = {5: 50, 6: 60}
    dictionary4 = {}

    for dictionary in (dictionary1, dictionary2, dictionary3):
        dictionary4.update(dictionary)

    print(f"Dictionary 1: {dictionary1}")
    print(f"Dictionary 2: {dictionary2}")
    print(f"Dictionary 3: {dictionary3}")
    print(f"Final dictionary: {dictionary4}")


def check_key():
    """Ques no.30: Write a Python script to check whether a given key already exists in a
    dictionary.

    """

    #Code
    dictionary = {1: 10, 2: 20}

    key = int(input("Enter key: "))

    print(f"Dictionary: {dictionary}")
    if key in dictionary.keys():
        print("The key exists.")
    else:
        print("The key does not exist")


def interate_dictionary():
    """
    Ques no.31: Write a Python program to iterate over dictionaries using for loops.

    """

    #Code
    dictionary = {'username': 'Lolem', 'id': 14782, 'friend_list': ['ram', 'shyam', 'hari']}
    print(f"Dictionary = {dictionary}")
    for key, value in dictionary.items():
        print(f"The key is {key} and value is {value}.")


def squared_dict_generator():
    """
    Ques no.32: Write a Python script to generate and print a dictionary that contains a
    number (between 1 and n) in the form (x, x*x).

    """

    #Code
    number_of_terms = int(input("Enter the number of terms you want: "))
    dictionary = {}

    for key in range(1,number_of_terms+1):
        dictionary[key] = pow(key, 2)

    print(f"Required Dictionary = {dictionary}")


def squared_dict_generator_15():
    """
    Ques no.33: Write a Python script to print a dictionary where the keys are numbers
    between 1 and 15 (both included) and the values are square of keys

    """

    #Code
    dictionary = {}

    for key in range(1,16):
        dictionary[key] = pow(key, 2)

    print(f"Required Dictionary = {dictionary}")


def merge_dictionary():
    """
    Ques no.34: Write a Python script to merge two Python dictionaries.

    """

    #Code
    dictionary1 = {'username': 'Lolem', 'id': 14356}
    dictionary2 = {'number': 9876543210, 'address': 'abc'}

    print(f"Dictionary1 = {dictionary1}")
    print(f"Dictionary2 = {dictionary2}")

    for key, value in dictionary2.items():
        dictionary1[key] = value

    print(f"Merged dictionary = {dictionary1}")


def sum_of_items():
    """
    Ques no.36: Write a Python program to sum all the items in a dictionary.

    """

    #Code
    dictionary = {1: 1, 2: 4, 3: 9, 4: 16}
    sum = 0
    for value in dictionary.values():
        sum += value
    
    print(f"Dictionary = {dictionary}")
    print(f"The sum is {sum}.")


def mul_of_items():
    """
    Ques no.37: Write a Python program to multiply all the items in a dictionary.

    """

    #Code
    dictionary = {1: 1, 2: 4, 3: 9, 4: 16}
    mul= 1
    for value in dictionary.values():
        mul *= value
    
    print(f"Dictionary = {dictionary}")
    print(f"The multiplication is {mul}.")


def remove_key():
    """
    Ques no.38: Write a Python program to remove a key from a dictionary.

    """

    #Code
    dictionary = {'username': 'Lolem', 'id': 14782, 'friend_list': ['ram', 'shyam', 'hari']}
    print("The available keys are: ")
    for key in dictionary.keys():
        print(key)

    key = input("Enter the key you want to delete: ")
    try:
        dictionary.__delitem__(key)
        print("Deleted sucessfully")
        print(dictionary)
    except KeyError:
        print("No such key!")


def unpack_tuple():
    """
    Ques no.39: Write a Python program to unpack a tuple in several variables.

    """

    #Code
    some_tuple = (1, 2, 3, 4, 5)
    num1, num2, num3, num4, num5 = some_tuple

    print(f"Given tuple: {some_tuple}")
    print("Unpacking..")
    print(f"num1 = {num1}\nnum2 = {num2}\nnum3 = {num3}\nnum4 = {num4}\nnum5 = {num5}\n")


def add_item_tuple():
    """
    Ques no.40: Write a Python program to add an item in a tuple.
    
    """

    #Code
    some_tuple = (1, 2, 3, 4)
    print(f"Original tuple: {some_tuple}")
    add = int(input("Enter number to add in the tuple: "))
    some_tuple += (add,)

    print(f"After adding: {some_tuple}")




functions = {
    1: character_frequency, 
    2: manipulate_string,
    3: change_repeated, 
    4: swap_string,
    5: ing_adder, 
    6: not_poor,
    7: longest_string, 
    8: remove_char,
    9: exchange, 
    10: remove_odd_index,
    11: word_count, 
    12: change_to_uppper_and_lower,
    13: unique_words_sorted, 
    14: add_tags,
    15: insert_string_in_middle, 
    16: sum_of_list,
    17: multiplication_of_list, 
    18: largest_in_list,
    19: smallest_in_list, 
    20: string_with_same_letters,
    21: sorted_tuple_list, 
    22: remove_duplicates,
    23: empty_list_check, 
    24: clone_list,
    25: check_empty_list_of_dict, 
    26: insert_string_in_start,
    27: adding_list, 
    28: update_dict,
    29: concatenate_dicts, 
    30: check_key,
    31: interate_dictionary, 
    32: squared_dict_generator,
    33: squared_dict_generator_15, 
    34: merge_dictionary,
    35: interate_dictionary, 
    36: sum_of_items,
    37: mul_of_items, 
    38: remove_key,
    39: unpack_tuple, 
    40: add_item_tuple,
    41: None, 
    42: None,
    43: None, 
    44: None,
    45: None, 
    46: None
}
