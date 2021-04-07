# 1. Class and object
# 2. Inheritance
# 3. Encapsulation
# 4. Polymorphism
# 5. Abstraction
# 6. Accessor and mutator function (Getter and Setter)
# 7. Access modifier (public, private, protected)

# 1. Class and object
    # -> noun
# => state (characterstics, property)
    # -> adjective
# => behaviour (action, function)
    # -> verb

# Car,
#     color, model, manuf_year,
#     start, stop, run

# class Car:
#     # Initialiser function
#     def __init__(self, name, color, year):
#         self.name = name
#         self.color = color
#         self.year = year

#     def start(self):
#         print(f"{self.name} started.")

#     def stop(self):
#         print(f"{self.name} stopped.")

# c = Car("BMW", "BLACK", "2021")
# print(c.__dict__)
# TypeError: __init__() missing 3 required positional arguments: 'name', 'color', and 'year'

# class Laptop:

#     def __init__(self, brand, color, ram="2 GB"):
#         # instance variable
#         self.brand = brand
#         self.color = color
#         self.ram = ram

#     # instance method
#     def reboot(self):
#         print(f"{self.brand} laptop is rebooting.")

# l = Laptop("Lenovo", "Black", "16 GB")
# print(l.ram)

# dell = Laptop("Dell", "Silver")
# print(dell.ram)

# l.reboot()
# dell.reboot()

# class Calculator:

#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         return self.num1 + self.num2

#     def difference(self):
#         return self.num1 - self.num2

#     def product(self):
#         return self.num1 * self.num2

#     @staticmethod
#     def square_root(num):
#         return num ** 0.5

# c = Calculator(19, 10)
# # print(c.add())
# # print(c.difference())
# # print(c.product())
# print(Calculator.square_root(100))

# class Student:

#     # class or static variable
#     college_name = "ABC College"

#     def __init__(self, _id, name, address):
#         self._id = _id
#         self.name = name
#         self.address = address

# s = Student("001", "Ram", "Ktm")
# # print(s._id, s.name, s.address)
# print(s.college_name)
# print(s.__dict__)

# st = Student("002", "Shyam", "Pkr")
# print(st.college_name)
# print(st.__dict__)
# print(Student.college_name)


# class Product:

#     shop_name = "ABC Shop"

#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price # Name Managaling "_Product__price"
#         # _ClassName__attrname

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price

#     def __str__(self):
#         return f"{self.name} => {self.price}"

#     def __eq__(self, obj):
#         return self.__price == obj.__price

    # def get_price(self):
    #     return self.__price

    # def set_price(self, price):
    #     if price > 0:
    #         self.__price = price

# pant = Product("Pant", 1600)
# tshirt = Product("Tshirt", 1600)
# print(pant==tshirt)
# print(dir(Product))
# print(dir(str))
# print(p.get_price())
# p.set_price(100)
# print(p.get_price())
# print("Initial Value", p.price)
# p.price = 1900
# p.name
# print("Final Value", p.price)
# print(p)