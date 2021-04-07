# if <condition>:
    # instruction

# if False:
#     print("This is if statement")
# else:
#     print("This is else statement")

# num = int(input("Enter any number: "))
# if num > 0:
#     print("This is positive number.")
# else:
#     print("This is negative number.")

# num = int(input("Enter any number: "))
# rem = num % 2
# if rem == 0:
#     print("This is even number.")
# else:
#     print("This is odd number.")

# user input, convert to int
# if number is exactly divided by 3,
# print("Exactly divided by 3")
# same goes for 5 and 7

# num = int(input("Enter any num: "))
# if num % 3 == 0:
#     print("Exactly divided by 3")
# elif num % 5 == 0:
#     print("Exactly divided by 5")
# elif num % 7 == 0:
#     print("Exactly divided by 7")

# num1 = int(input("Enter any num: "))
# num2 = int(input("Enter any num: "))
# if num1 > num2:
#     print(num1, "is greatest.")
# elif num2 > num1:
#     print(num2, "is greatest.")

# num1 = int(input("Enter any num: "))
# num2 = int(input("Enter any num: "))
# num3 = int(input("Enter any num: "))

# if num2<= num1 >=num3:
#     print(num1, "is greatest")
# elif num1 <= num2 >= num3:
#     print(num2, "is greatest")
# else:
#     print(num3, "is greatest")

num1 = int(input("Enter any num: "))
num2 = int(input("Enter any num: "))
num3 = int(input("Enter any num: "))

if (num2 <= num1 >= num3 and num1 >= num2 <= num3) or (num2 >= num1 <= num3 and num1 <= num2 >= num3):
    print(num1 + num2)
elif (num1 <= num2 >= num3 and num1 >= num3 <= num2) or (num1 >= num2 <= num3 and num1 <= num3 >= num2):
    print(num2 + num3)
else:
    print(num1 + num3)