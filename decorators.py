# def decorate_function(f):
#     def wrapper():
#         print("Nice to see you.")
#         f()
#         print("Welcome again.")
#     return wrapper

# @decorate_function
# def greet():
#     print("Welcome Home.")

# w = decorate_function(greet)
# w()
# greet()

def smart_division(func):
    def wrapper(num1, num2):
        print(f"func: {func}")
        if num2 == 0:
            return "Could not divide by zero"
        else:
            return func(num1, num2)
    return wrapper

@smart_division
def division(num1, num2):
    return num1 / num2

# print(division(10, 10))
print(division(2, 0))
print(f"Division: {division}")


def admin_required(func):
    def wrapper():
        if user is admin and user is salesperson:
            return func()
        else:
            "invalid request"

def product_list():
    pass

@admin_required
def sales_report():
    pass

@admin_required
def product_pricing_history_report():
    pass