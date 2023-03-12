# a = "15"
# b = int(a)
# c = 3
#
# print(a, type(a))
# print(b, type(b))
#
# # print("Valid instruction.")

# user_input = input("insert a number:")
# user_input = int(user_input)
# print(user_input, type(user_input))

# user_input = input("insert a number:")
#
# # try:
# #     user_input = int(user_input)
# #     print(undefined value)
# # except ValueError as e:
# #     print(e)
# #     print(f"Your inserted '{user_input}' which is not a valid number")
# #
# # print("Valid instruction")
#
# # try:
# #     user_input = int(user_input)
# #     print(undefined_value)
# # except (ValueError, Exception) as e:
# #     print("I caught the following exception:", e, type(e))
# #
# #
# # print("Valid instruction")
#
# # try:
# #     user_input = int(user_input)
# #     print(undefined_value)
# # except ValueError as e:
# #     print("I caught a valueError exception:", e)
# # except NameError as e:
# #     print("I caught the following exception:", e)
# #
# # print("Valid instruction")
#
# try:
#     user_input = int(user_input)
#
# except ValueError as e:
#     print("I caught a valueError exception:", e)
#
#
# print("Valid instruction")

# user_name = input("Name:")
# print("Name:", user_name)
#
# user_age = input("Age:")
# try:
#     print("Age:", int(user_age))
# except ValueError:
#     print("Age:", user_age, "this is a invalid value")
#
# user_city = input("City:")
# print("City:", user_city

# user_age = input("age:")

# try:
#     user_age = int(user_age)
#
#     if user_age > 18:
#         print("you are a grown up!")
#
# except ValueError:
#     print("Invalid age")

# user_age = input("age:")

# try:
#     user_age = int(user_age)
# except ValueError:
#     print("Invalid age")
#
# if (type(user_age) == int) and (user_age >= 18):
#     print("you are a grown up!")

# user_age = input("age:")
#
# try:
#     user_age = int(user_age)
# except ValueError:
#     print("Invalid age")
# else:
#     if user_age >= 18:
#         print("you are a grown up!")
#     else:
#         print("you are a child")
#
# finally:
#     print("End of program")

# user_age = int(input("age:"))
#
# if user_age < 14:
#     print("you dont have an ID")
# elif user_age < 18:
#     print("you are a child")
# elif user_age < 65:
#     print("you are a grown up")
# else:
#     print("you are retired")

# my_numbers = [54, 23, 54, 78, -2] # leng(my_numbers) = 4

# for item in my_numbers:
#     print(f"item with value = {item} is on index = {my_numbers.index(item)}")

# print(list(enumerate(my_numbers)))

# for element in enumerate(my_numbers):
#     # print(element, type(element))
#     print(f"item with value = {element[1]} is on index = {element[0]}")

# my_tuple = (56, -2, 14)
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# for index, number in enumerate(my_numbers):
#     print(f"item with value = {number} is on index = {index}")

# my_numbers = [54, 23, 54, 78, -2]
# index = 0
#
# while index <len(my_numbers):
#     print(f"items with value = {my_numbers[index]} is on index = {index}")
#     index = index + 1


# is_valid_age = False
#
# while not is_valid_age:
#
#     try:
#         age = int(input("Age:"))
#     except ValueError:
#         print("Invalid age")
#     else:
#         is_valid_age = True
#
#         if age >= 18:
#             print("you are a grown up!")
#         else:
#             print("you are a child")

# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if number % 2 == 0:
#         print(f"number = {number} is even")
#         break
#
#     print(f"number = {number} is odd")


while True:

    try:
        age = int(input("Age:"))
    except ValueError:
        print("Invalid age")
        continue


    if age >= 18:
        print("you are a grown up!")
    else:
        print("you are a child")

    break
