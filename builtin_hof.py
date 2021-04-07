# map and filter

# lambda function
# def a(x1, x2, x3):
#     return x1 + x2 + x3

# a = lambda x1, x2, x3: x1 + x2 + x3
# print(a(6, 7, 8))

# map(function, iterable_object)

# a = [2, 4, 6, 8, 10, 12, 14, 16]
# def increase_by_one(n):
#     return n+1

# b = map(lambda n:n+1, a)
# print(list(b))

# namelist = ["ram", "shyam", "hari", "geeta", "harry"]
# # result = ["Ram", "Shyam", "Hari", "Geeta", "Harry"]
# result = list(map(lambda name:name.title(), namelist))
# print(result)

# emaillist = ["1-gmail.com", "2-gmail.com", "3-gmail.com", "4-gamil.com"]
# # res = ["1@gmail.com", "2@gmail.com", "3@gmail.com", ...]
# res = list(map(lambda email: email.replace("-", "@"), emaillist))
# print(res)

# filter(func, iterable_object)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda n: n % 2 == 0, a)
print(list(even))

emaillist = ["1@gmail.com", "2@gmail.com",
            "3@gmail.com", "4@hotmail.com",
            "5@yahoo.com", "6@gmail.com",
            "7@yahoo.com",
            ]
res =filter(lambda email:email.endswith("gmail.com"), emaillist)
print(list(res))