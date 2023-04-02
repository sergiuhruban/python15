# def get_numbers():
#    for element in range(10):
#        yield element
#
#
# # my_sequence = get_numbers()
#
# # for element in my_sequence:
#
# print(next(my_sequence))

# def get_numbers():

# import sys
#
#
# my_list = [element for element in range(10)]
# print(type(my_list), sys.getsizeof(my_list))
#
# my_generator = (element for element in range(10))
# print(type(my_generator), sys.getsizeof(my_generator))



# if __name__ == '__main__':
#     # file = open("/Users/sergiuhruban/PycharmProjects/python15/generators_and_files/data.txt", "r")
#     file = open("data.txt", "r")
#     line = file.readline()
#     print(line)
#     line = file.readline()
#     print(line)
#     file.close()
#
#
#     line = file.readline()
#     print(line)

# if __name__ == '__main__':
#     with open("data.txt") as file:
#         # content = file.read()
#         # lines = file.readlines()
#         lines = (line for line in file.readlines())
#
#     print(type(lines))
#
#     for line in lines:
#         print(line.replace("\n", ""))

# if __name__ == '__main__':
#     with open("data.txt", "w") as file:
#         # file.write("Heloo world")
#         file.writelines([
#             "Hello world! \n",
#             "Hello world! \n",
#             "Hello world! \n",
#             "Hello world! \n",
#             "Hello world! \n",
#             "Hello world! \n",
#
#         ])

if __name__ == '__main__':
    with open("data.txt", "w") as file:
        file.write("Append line a1")
        file.writelines([
            "Append line a2\n",
            "Append line a3\n",
            "Append line a4\n",
        ])











