
attempts = 3
for i in range(attempts):
    try:
        age = int(input('Age:'))
        print(f'Your age is:{age}')
        break
    except ValueError:
        if i == attempts - 1:
            print("Maximum number of attempts fave been reached. See you net time")



