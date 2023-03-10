# def my_first_function():
#     print("Hello from my first function")
#
#     print("sum of 5 + 7", 5 + 7)
#
#
#
# print('--BEFORE FUNCTION CALL')
# my_first_function()
# print('--AFTER FUNCTION CALL')

# def show_sum_of_numbers():
#     while True:
#         try:
#             a = int(input("a = "))
#             break
#         except ValueError:
#             print("Value for a is not a number. Try again")
#
#     while True:
#         try:
#             b = int(input("b = "))
#             break
#         except ValueError:
#             print("Value for a is not a number. Try again")
#
#
#     print(f"Sum of {a} and {b} is {a + b}")
#
#
# show_sum_of_numbers()
# show_sum_of_numbers()
# show_sum_of_numbers()



# def get_number():
#     number = int(input("number: "))
#     return number
#
# a = get_number()
# b = get_number()
#
# print("Sum = ", a + b)



# def get_number_from_user():
#     number = in(input("number:"))
#
# def show_sum_of_numbers():
#     while True:
#         try:
#             get_number_from_user()
#             break
#         except ValueError:
#             print("Value for a is not a number. Try again")
#
#     while True:
#         try:
#             get_number_from_user()
#             break
#         except ValueError:
#             print("Value for a is not a number. Try again")
#
#
#     print(f"Sum of {a} and {b} is {a + b}")
#
#
# show_sum_of_numbers()

# def do_math(a, b, operation="+"):
#     if operation == "*":
#         return a * b
#
#     if operation == "/":
#         return a / b
#
#     if operation == "-":
#         return a - b
#
#     return a + b
#
# print(do_math(3, 7))
# print(do_math(4, 7, operation="*"))


# def f(a, b ,c, *args): #variable length arguments
#     print(a, b, c, args)
#
# # f()
# # f(10, 5)
# f(10, 5, 6, 7, 9)
# f(4, 5, 6, 7, 78, 8)


# def f(*args, **kwargs): #keyword variable length arguments
#     print(args, kwargs)
#
# f()
# f(1, 2, 3)
# f(1, 2, 3, 4)
# f(1, 2, 3, 4, 5, p1=2, p2="abc")
# f(1, 2, 3, 43, 4, p1=2, p3="123", p4=[1,2])

# def f(a, b):
#     return a + b
#
# a = f
#
# print(a(2, 7))

# my_variable = 10
#
# def f1():
#     print("my variable inside f1"my_variable)
#
#
# f1()

# def f():
#     print("inside")
#     f()
# f()

# def f(n):
#     print(n)
#
#
#
#     if n == 0:
#         return
#
#     f(n - 1)
#
# f(5)

