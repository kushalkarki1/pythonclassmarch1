try:
    num1 = int(input("Enter any number: "))
    num2 = int(input("Enter another number: "))
    # print(n)
except ValueError:
    print("input must be number.")
except NameError as err:
    print(err)
else:
    print(f"Sum of {num1} and {num2} is {num1+num2}.")
finally:
    print("Completed")

name = input("Enter your name: ")
print(f"Your name is {name}")
print("Program completed")

# try:
#     pass
# except Exception:
#     pass
# except Exception:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass