# my_list = [] # my_list = list()

# my_numbers = [2, 4, -3, 12, 10, -15]
#
# my_numbers = ['a', 'b', 'c', 'd', 'e', 'f']
# #              0    1    2    3    4    5
# #             -6   -5   -4   -3   -2   -1

#
# print(my_numbers[1])
# print(my_numbers[-1])
#
# print("length of the list =", len(my_numbers))


# my_numbers = ['a', 'b', 'c', 'd', 'e', 'f']
# #              0    1    2    3    4    5
# #             -6   -5   -4   -3   -2   -1
#
# # slice: my_numbers[start:end:step]
#
# # my_slice = my_numbers[::]
# # my_slice = my_numbers[0:len(my_numbers):1]
# # my_slice = my_numbers[1:4:1]
# # my_slice = my_numbers[1:4:2]
# # my_slice = my_numbers[4:2:-1]
# # my_slice = my_numbers[::-1]
# my_slice = my_numbers[1:]
# print("my_numbers", my_numbers, type(my_numbers))
# print("my_slice", my_slice, type(my_slice))

# my_numbers = ['a', 'b', 'c', 'd', 'e', 'f']
# print(my_numbers)
# my_numbers.append('g')
# my_numbers.insert(1, 'h')
# print(my_numbers)

# my_string = "Ana are mere"
# print(my_string[1:])
# my_list = list(my_string)
# print("my_list=", my_list)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b is b, a is not b)
# a.append(4)
# print(a == b is b, a is b)

# my_string = "mere pere struguri"
# my_list = my_string.split(" ")
# print(my_list, type(my_list))
# # my_string = " ".join(my_list)
# print(my_string, type(my_string))

# my_tuple = (1, 2, 3)
# print('my_tuple', my_tuple)
# my_list = list(my_tuple)
# print(my_list)
# my_list.append(4)
# my_tuple = tuple(my_list)
# print('my_tuple', my_tuple)

# my_tuple = (1, 2, 3)
# my_tuple = (1, 2, 3, 4)
# print(my_tuple)

# a = (1, 2, 3)
# c = a
# a = (1, 2, 3, 4)
# print(c)

# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200,
# }
#
# print(my_dict["age"])
#
# my_dict["age"] = 31
# print(my_dict["age"])
# print(my_dict)
# del my_dict["height"]
# print(my_dict)

# student_1 = {"name": "Mihai"}
# student_2 = {"name": "Sergiu"}
# student_3 = {"name": "Elena"}
#
# students = [student_1, student_2, student_3]
# print(students)
# student_1["promoted"] = True
# print(students)

# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200,
# }
#
# print(list(my_dict.keys()))
# print(list(my_dict.values()))
# print(list(my_dict.items()))

# print("are" in "Ana are mere")
# print(10 in [1, 10, 20])
# print("name" in {"name": "Mihai", "age": 30})
# print("Mihai" in {"name": "Mihai", "age": 30}.values())

# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200,
# }
#
# print(my_dict.get("country", None)) #luarea valorii unei chei
# print(my_dict.get("city")) #luarea valorii unei chei

# my_set = {} #is a empty dictionary
# print(type(my_set))

# my_set = {1, None, True, False, 0,  "abc", "aaa"}
# # print(my_set, type(my_set))
# # print(True in my_set)
# print(hash(1))
# print(hash(True))
# print(hash(False))
# print(hash(0))

# my_list = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# my_list.pop()
# print(my_list)

# my_set = {1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}
# # my_set.pop()
# print(my_set)
# print(len(my_set))

# my_set_1 = {1, 2, 3}
# my_set_2 = {2, 3, 4}
# # print(my_set_1.union(my_set_2))
# # print(my_set_1.intersection(my_set_2))