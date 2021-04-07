# def func(*args):
#     print(args)

# func(1, 2, 3, "python", "PHP")

# def func_new(**kwargs):
#     print(kwargs)

# func_new(name="Ram", contact="92372")

# def func(*args, **kwargs):
#     print(args, kwargs)

# func(1, 2, 3, 4, name="Ram", contact="3232")


# def welcome():
#     print("Welcome Ram")

# w = welcome
# w()

# def welcome(name):
#     print(f"Welcome {name}")

# def namaste(name):
#     print(f"Namaste {name}")

# def greet(f, name):
#     # 34-> w = welcome, name = Ram
#     # 35-> w = namaste, name = Shyam
#     f(name)

# greet(welcome, "Ram")
# greet(namaste, "Shyam")

# a = 10

# def main():
#     def inner_func():
#         print("I am inner function.")

#     return inner_func

# in_func = main()
# in_func()
# in_func()

# def main(n):
#     def addition(a , b):
#         return a + b
#     def subtraction(a, b):
#         return a - b
#     if n == 1:
#         return addition
#     elif n == 2:
#         return subtraction

# add = main(1)
# print(add(10, 9))

# sub = main(2)
# print(sub(10, 8))


# num = 10 # Immutable object

# def main_function():
#     global num
#     num = num + 1
#     print(num)

# main_function()

# alist = [1, 2]

# def main():
#     alist.append(5)

# print(alist)
# main()
# print(alist)

num = 5

def main():
    num = 10
    def inner_func():
        nonlocal num
        num = num + 1
        print(num)
    inner_func()

main()