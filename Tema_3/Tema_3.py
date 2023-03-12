# Problema 3

# def read_integer():
#     number = input("Enter a number:")
#     try:
#         value = int(number)
#         return value
#     except ValueError:
#         return 0
#
# # Problema 2
#
# def get_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + get_sum(n - 1)

# Problema 1

def sum_numbers(*args, **kwargs):
    s = 0
    for param in args:
        try:
            s += float(param)
        except (TypeError, ValueError):
            break
    for param in kwargs.values():
        try:
            s += float(param)
        except (TypeError, ValueError):
            break
    return s


sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad'])
sum_numbers()
sum_numbers(2, 4, 'abc', param_1=2)
