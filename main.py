

# The Idea for this project is to make a basic calculator in the terminal
# The properties of this calculator for now will be -
# adding , multiplying, dividing, and subtracting using PEMDOS rules
# I'd like the user to be able to just enter 4*5 and it calculates, -
# instead of having it run options, like "enter 1 number" etc.
import os.path
item = ""
i = ""
operator = ""
num1 = 1
num2 = 2


def calc_name():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # print(dir_path)
    # Notes: trying to capture the path of this file,
    # and then have this say Welcome To (filename) of current file.
    path_list = dir_path.split('/')
    # print(path_list)
    # I'm trying to capture the index number of the "2-Basic-Calc" and then have only that displayed.
    global item
    global i
    for i, item in enumerate(path_list, start=1):
        if i == 6:
            break


calc_name()

print("Welcome to " + item)


def validate_numeric(value_string, numeric_type=float):
    try:
        return numeric_type(value_string)
    except ValueError:
        raise


def user_operator():
    global operator
    # operator_list = {
            #'+': calculator(),
            #'-': calculator(),
            #'*': calculator(),
            #'/': calculator(),
            #'^': calculator()}
    operator = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ^ for exponentiation
    ''')
    # if operator in operator_list:
    #    pass
    #else:
    #    print("Invalid Operator! Please run again!")
    #    user_operator()
    if operator == "+":
        calculator()
    elif operator == "-":
        calculator()
    elif operator == "*":
        calculator()
    elif operator == "/":
        calculator()
    elif operator == "^":
        calculator()
    else:
        print("Invalid operator! Please type a correct operator! Halting program...")
        rerun()


def calculator():
    global num1
    global num2
    while True:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            result = validate_numeric(num1, float)
            result = validate_numeric(num2, float)
        except ValueError:
            print("Incorrect format. Please input a integer.")
            continue
        else:
            break

    if operator == "+":
        print('{} + {} = '.format(num1, num2) + str(num1 + num2))
    elif operator == "-":
        print('{} - {} = '.format(num1, num2) + str(num1 - num2))
    elif operator == "*":
        print('{} * {} = '.format(num1, num2) + str(num1 * num2))
    elif operator == "/":
        print('{} / {} = '.format(num1, num2) + str(num1 / num2))
    elif operator == "^":
        print('{} ^ {} = '.format(num1, num2) + str(num1 ** num2))
    else:
        print("Invalid input. Re-running program...")
        calculator()
    rerun()


def rerun():
    user_yes = ['yes', 'ye', 'yea','yeah', 'y']
    user_no = ['no', 'nah', 'nope', 'n']
    re_run = input("Would you like to calculate again?\n: ")
    if re_run.lower() == user_yes:
        calc_name()
    elif re_run.lower() == user_no:
        print("Thank you for using Basic Calc!")
    else:
        print("Invald input, please try again!")
        rerun()


user_operator()
