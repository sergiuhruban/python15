

for i in range(3):§
    try:
        age = int(input('Age:'))
        print(f'Your age is:{age}')

    except ValueError:
        print("Invalid input, try again")

else:
    print("Maximum number of attempts fave been reached. See you net time")



