
# def read_integer():
#     number = input("Enter a number:")
#     try:
#         value = int(number)
#         return value
#     except ValueError:
#         return 0
#
#
# def get_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + get_sum(n - 1)
# get_sum(50)
#
# def sum_even(n):
#     if n == 0:
#         return 0
#     elif n % 2 != 0:
#         return sum_even(n - 1)
#     else:
#         return n + sum_even(n - 2)
# sum_even(9)


# def sum_numbers(*args, **kwargs):
#     s = 0
#     for param in args:
#         try:
#             s += float(param)
#         except (TypeError, ValueError):
#             pass
#     for param in kwargs.values():
#         try:
#             s += float(param)
#         except (TypeError, ValueError):
#             pass
#
#     return s
#
#
# sum_numbers(1, 5, -3, "abc", [12, 56, "cad"])
# sum_numbers()
# sum_numbers(2, 4, "abc", param_1=2)



def sum_numbers(*args, **kwargs):
    s = 0
    for param in args + tuple(kwargs.values()):
        try:
            s += float(param)
        except (TypeError, ValueError):
            pass
    return s

print(sum_numbers(1, 5, -3, "abc", [12, 56, "cad"]))
print(sum_numbers())
print(sum_numbers(2, 4, "abc", param_1=2))

def sum_numbers(*args, **kwargs):
    total = 0
    for param in kwargs.values():
        try:
            total += int(param)
        except (ValueError, TypeError):
            try:
                total += float(param)
            except (ValueError, TypeError):
                pass
    return total

print(sum_numbers(1, 5, -3, "abc", "12", [12, 56, "cad"]))
print(sum_numbers(1, 5, -3, "abc", "12", [12, 56, [1, 2], "cad"]))
print(sum_numbers(1, 5, -3, "abc", "12", [12, 56, [1, 2, {3, 4}], "cad"]))
print(sum_numbers())
print(sum_numbers(2, 4, "abc", param_1=2))
print(sum_numbers(2, 4, "abc", param_1=2, param_2="abc"))
print(sum_numbers(2, 4, "abc", param_1=2, param_2="abc", param_3=2.5))


def sum_numbers(*args, **kwargs):
    s = 0
    for arg in args + tuple(kwargs.values()):
        if type(arg) in (int, float):
            s += float(arg)
        elif type(arg) in (list, tuple, set):
            s += sum_numbers(*arg)
        elif type(arg) is dict:
            s += sum_numbers(*arg.values())
    return s

print(sum_numbers(1, 5, -3, "abc", "12", [12, 56, "cad"]))
print(sum_numbers(1, 5, -3, "abc", "12", [12, 56, [1, 2], "cad"]))
print(sum_numbers(1, 5, -3, "abc", "12", [12, 56, [1, 2, {3, 4}], "cad"]))
print(sum_numbers())
print(sum_numbers(2, 4, "abc", param_1=2))
print(sum_numbers(2, 4, "abc", param_1=2, param_2="abc"))
print(sum_numbers(2, 4, "abc", param_1=2, param_2="abc", param_3=2.5))
