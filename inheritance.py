# child class "IS A" parent class

# class Person:

#     def __init__(self, name, address, contact):
#         self.name = name
#         self.address = address
#         self.contact = contact

#     def walk(self):
#         print(f"{self.name} is walking.")

# class Student(Person):

#     def __init__(self, name, address, contact):
#         super().__init__(name, address, contact)

# class Teacher(Person):

#     def __init__(self, name, address, contact):
#         super().__init__(name, address, contact)

# s = Student("Ram", "Ktm", "98765432")
# # print(s.__dict__)
# s.walk()
# t= Teacher("Shyam", "Ktm", "123456789")
# t.walk()


# class Bird:
#     def __init__(self, name):
#         self.name = name

#     def fly(self):
#         print(f"{self.name} is flying.")

# class Pigeon(Bird):
#     def __init__(self, name):
#         super().__init__(name)

# class Ostrich(Bird):
#     def __init__(self, name):
#         super().__init__(name)

#     def fly(self):
#         print(f"{self.name} could not fly.")

# class HummingBird(Bird):
#     def __init__(self, name):
#         super().__init__(name)

#     def fly(self):
#         super().fly()
#         print("It can also fly backward.")

# p = Pigeon("Robot")
# p.fly()
# ost = Ostrich("Horse")
# ost.fly()
# h = HummingBird("Tiny")
# h.fly()

class User:
    def __init__(self, _id, username, password):
        self._id = _id
        self.username = username
        self.password = password

    def login(self, username, password):
        # Implement this function
        # Student and Teacher object should be able to log in
        if username == self.username and password == self.password:
            print("Login successful")
            return True
        else:
            print("Invalid Login")
            return False

class Person(User):
    def __init__(self, _id, username, password, name, contact, address):
        super().__init__(_id, username, password)
        self.name = name
        self.contact = contact
        self.address = address

    def display_profile(self):
        # Implement this function
        # _id, username, contact, address, name
        # course if person is Student
        # designation if person is Teacher
        print(f"Id: {self._id} \nusername: {self.username}\ncontact: {self.contact}\naddress: {self.address}\nname:{self.name}")

class Student(Person):
    def __init__(self, _id, username, password, name, contact, address, course):
        super().__init__(_id, username, password, name, contact, address)
        self.course = course

    def display_profile(self):
        super().display_profile()
        print(f"course: {self.course}")

class Teacher(Person):
    def __init__(self, _id, username, password, name, contact, address, designation):
        super().__init__(_id, username, password, name, contact, address)
        self.designation = designation

    def display_profile(self):
        super().display_profile()
        print(f"designation: {self.designation}")

st = Student("001", "a", "p", "Ananta", "987654", "Ktm", "Python")
uname = input("Enter username: ")
pwd = input("Enter password: ")
if st.login(uname, pwd):
    st.display_profile()

# t = Teacher("002", "aa", "pp", "Ananta", "987654", "Ktm", "Professor")
# uname = input("Enter username: ")
# pwd = input("Enter password: ")
# if t.login(uname, pwd):
#     t.display_profile()