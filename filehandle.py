# r, w, a

# f = open("test.txt", "w")
# f.write("Hello, I am Python Here.\n")
# f.close()

# f = open("test.txt", "a")
# f.write("Hey there, I am new in python.")
# f.close()

# f = open("test.txt", "r")
# print(f.read())
# f.close()

# f = open("test.txt", "r")
# print(f.readline())
# f.close()

# f = open("test.txt", "r")
# print(f.readlines())
# f.close()

a = [
        {"1":
            {
            "name": ["Ram", "Kumar", "Shrestha"],
            "contact":
                {
                "home":["01-556677"],
                "office":["01-665577"]
                },
            },
            "friends":[
                {"2":
                    {
                    "name": ["Shyam", "", "Joshi"],
                    "contact":
                        {
                        "home":["01-999999"],
                        "office":[""]
                        }
                    }
                }
            ]
        },
    ]
# Your name is Ram Kumar Shrestha
# Your home contact is 01-556677
# Your office contact is 01-66557
fullname = a[0].get("1").get("name")
print(f"Your name is {' '.join(fullname)}.")
print(a[0].get("1").get("contact").get("home")[0])
print(a[0].get("1").get("contact").get("office")[0])