# for <variable> in <iterable_object>:
    # code to be repeated

# a = [6, 9, 10, 14, 15]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# for item in a:
#     print(item)

# for i in range(100):
#     print(i)

# range(start, stop, step)
# range(100):
    # start->0, stop->99, step->1
# range(1, 100)
    # start->1, stop->99, step->1
# range(1, 100, 2)
    # start->1, stop->99, step->2
    # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ...

# a = []
# for i in range(10):
#     b = input("Enter anything: ")
#     a.append(b)

# print(a)

# total_sum = 0
# for i in range(10):
#     num = int(input("Enter any number: "))
#     total_sum += num # total_sum = total_sum + num

# print(f"Total sum is {total_sum}")

# mainlist, duplicatelist, evenlist, oddlist
# take 15 userinput and cast to int
# if number is even append to evenlist,
# if odd append to oddlist
# all userinput must be in mainlist
# if userinput repeated (duplicate entry), append it
# to duplicatelist

# mainlist, duplicatelist, evenlist, oddlist = [], [], [], []
# for i in range(15):
#     num = int(input("Enter any number: "))
#     if num in mainlist:
#         duplicatelist.append(num)
#     else:
#         if num % 2 == 0:
#             evenlist.append(num)
#         else:
#             oddlist.append(num)
#     mainlist.append(num)

# print(f"Main List: {mainlist}")
# print(f"Duplicate List: {duplicatelist} ")
# print(f"Even List: {evenlist}")
# print(f"Odd List: {oddlist}")


# from 1 to 100
# print all numbers
# print "flip" if number is exactly divided by 3
# print "flop" if number is exactly divided by 5
# print "flip-flop" if number is exactly divided by 3 and 5

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("flip-flop")
#     elif i % 3 == 0:
#         print("flip")
#     elif i % 5 == 0:
#         print("flop")
#     else:
#         print(i)

# print(100//3)

# break , continue

for i in range(1, 20, 2):
    if i % 7 == 0:
        break
    print(i)

for i in range(1, 25):
    if i % 7 == 0:
        continue
    print(i)
