# import random
# import time
#
# if __name__ == '__main__':
#     print("I ll wait for 5 seconds:")
#     time.sleep(5)
#     print("I ll continue program execution: ")
#
#
#     my_numbers = [1, 3, 5, 7, 9, 12]
#     print(random.choice(my_numbers))


if __name__ == '__main__':
    while True:
        user_age = input("Age:")
        continue
        try:
            user_age = int(user_age)
        except ValueError:
            print("Invalid age, please try again.")

        if user_age <= 18:
            print("You do not have access here")
        else:
            print("Congrats! Acces granted")

        break