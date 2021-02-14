from DataTypes import Questions

print("Question number 1 - 46")
while True:
    check = input("Do you want to enter question number(Y/N): ")
    if check == 'n' or check == 'N':
        exit()
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
        except TypeError:
            print("Enter number!!")
        except KeyError:
            print("Question number does not exist!!")


dictionary ={1: 2, 3: 4}
function[1]