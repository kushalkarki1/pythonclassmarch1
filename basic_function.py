# def func_name():
    # body of function
    # instructions or code

# def func():
#     print("This is simple function.")

# func # call by reference
# func()

# def welcome(name): # name => parameter
#     print("Welcome", name)

# welcome("Ram") # Ram => argument
# welcome("Hari") # Hari => argument
# welcome("Shyam") # Shyam => argument

# def display_profile(name, contact, address):
#     print("Name", name)
#     print("Contact", contact)
#     print("Address", address)

# display_profile("Ram", "93732", "Ktm") # positional argument
# print("--------------------------------------------------")
# display_profile(name="Shyam", address="Pkr", contact="8376355")
# keyword argument

# def display_profile(name, contact, address, country="Nepal"):
#     print("Name", name)
#     print("Contact", contact)
#     print("Address", address)
#     print("Country", country)

# display_profile("Ram", "93732", "Ktm")
# print("--------------------------------------------")
# display_profile("Shyam", "8374", "Kabul", "Afganistan")

# def add(a, b, c):
#     print("Sum", (a+b+c))
#     print("Product", (a*b*c))

# add(8, 9, 10)

# function with return type
# and without return type

def add(num1, num2):
    total = num1 + num2
    return total

total_sum = add(6, 7)
print("Total sum", total_sum)