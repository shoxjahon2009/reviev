                    ### 1-masala
# txt = "A-sinf  B-sinf"
# x = txt.find("B")
# print(x)

            ## 2-masala
# def count(str):
#     vowels = "aeiou"
#     counts = 0
#     for x in str:
#         if x in vowels:
#             counts += 1
#     return counts
# print(count("shohjahon"))


        ## 3-masala
# filter_list = [1, 2, "a", "b"]
# a = [];
# for x in filter_list:
#     if type(x) == str:
#         a.append(x)
# print(a)

                ## 4-masala
# a = [5, 9, 10, 3, "J", "A", "W", 8, 5]
# b = []
# # count = 0
# for x in a:
#     if type(x) == int:
#         b.append(x)
#         # count += 1
# print(b)


            ### 5-masala
# list_1 = []
# list = ["A", 0, "Edabit", 1729, "Python", "1729"]
# for x in list:
#     if type(x) == int:
#         list_1.append(x)
# print(list_1)

                    ### 6-masala
# numbers = [1, 2, 3, 4, 5]
# a = list(enumerate(numbers))
# print(a)

#
# a = "incredible"
# b = a.replace("incredible","in...in..incredible ")
# print(b)

             ###   str  maslla


                ###  1-masala
# a = int(input("enter:"))
# if a == "Darth Vader":
#     print("Luke, I am your father.❗❗❗")
# elif a == "Leia":
#     print("Luke, I am your sister.❗❗")
# elif a == "Han":
#     print("Luke, I am your brother in law.❗")


            ## 2-masala

# a = input("enter:")
# if a == "happy":
#     print(f"Today, I am feeling {a}")
# elif a == "sad":
#     print(f"Today, I am feeling {a}")

                #  3 -masala
# def count(str):
#     vowels = "aeiou"
#     counts = 0
#     for x in str:
#         if x in vowels:
#             counts += 1
#     return counts
# print(count("shohjahon"))

            ### 4-masala

# a = ["Shohjahon"]
# for x in a:
#     b = x.replace("o","#")
#     print(b)



                    ###  list masalalar
# def get_budget(list):
#     a = 0
#     for x in list:
#         a += x["budget"]
#     return a
#
#
# print(get_budget([
#     {"name": "John", "age": 21, "budget": 29000},
#     {"name": "Steve", "age": 32, "budget": 32000},
#     {"name": "Martin", "age": 16, "budget": 1600}
# ]) )
             #  2
# def calc(list):
#     resault = 0
#     for x in list:
#         resault += x.count("#")
#     return resault
# print(calc([
#   "###",
#   "###",
#   "###"
# ]))

                    #  3
# a = int(input("son:"))
# b = [1,2,3,4,5,6,7]
# if a in b:
#      b.remove(a)
#      b.append(a)
# print(b)

                    ### 4

# a = {1,2,3,4,5}
# b  = a.remove(44)
# print(b)
#
# a = {1,2,3,4,5}
# b  = a.discard(44)
# print(b)

                  ###   5

# list = [9, 2, "space", "car", "lion", 16]
# a = []
# for x in list:
#     if type(x) == int:
#         a.append(x)
# print(a)


                    ### 6

# a = [1,2,3,3,5,4,5,1,7,7]
# b = []
# for x in a:
#     if x not in b:
#         b.append(x)
# print(b)


            ###  objekt masalalar


# def calc(list):
#     resaylr = {"HARIFLAR":0, "RAQAMLAR":0}
#     for x in list:
#         if x.isdigit():
#             resaylr ["RAQAMLAR"] += 1
#         elif x.isalpha():
#             resaylr["HARIFLAR"] += 1
#
#     return resaylr
#
# print(calc("MENI YOSHIM 15 DA"))

                                 ###   2
# def shop(list):
#     b = int(input("enter:"))
#     a = 0
#     for x in list.values():
#         a += x
#         y = a - b
#     return y
#
# print(shop({"skate": 200, "painting": 200, "shoes":1}))

                            # 3

