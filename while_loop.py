# Loop (Iteration)

# Bounded Loop - which have fix boundary
# of starting and ending. (for loop)

# Unbounded Loop - which do not have fix
# boundary for starting and ending. (while loop)

# while <condition>:
    # code to repeat

# choice = "y"
# while choice == "y":
#     num1 = int(input("Enter any number: "))
#     num2 = int(input("Enter another number: "))
#     print(f"Sum of {num1} and {num2} is {(num1+num2)}")
#     choice = input("Do you want to continue(y/n)? ")

# ask user for password
# print Invalid password until password is "abc1234"

# password = input("Enter password: ")
# while password != "abc1234":
#     print("Invalid password")
#     password = input("Enter password again: ")
# print("Successful entry")

# take two user input
# 1. addition 2. difference
# 3. product 4. division
# take user choice
# do u want to continue (y/n)

def addition(num1, num2):
    return num1 + num2

def difference(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

choice = "y"
while choice == "y":
    num1 = int(input("Enter any number: "))
    num2 = int(input("Enter another number: "))
    print("1.Sum \n2.Difference \n3.Product \n4.Division")
    operation_choice = input("Enter operation: ")
    if operation_choice == "1":
        print(addition(num1, num2))
    elif operation_choice == "2":
        print(difference(num1 ,num2))
    elif operation_choice == "3":
        print(product(num1, num2))
    elif operation_choice == "4":
        print(division(num1, num2))
    else:
        print("Invalid Operation Choice")
    choice = input("Do you want to continue(y/n)?")