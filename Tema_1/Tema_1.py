# declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

my_list.sort()
print(my_list)

my_asc_list = sorted(my_list)
print(my_asc_list)

# afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

my_list.sort(reverse=True)
print(my_list)

# afișează o listă ce conține numerele pare din lista ordonată (folosind slice)

my_even_list = my_list[::2]
print(my_even_list)

my_even_list = my_asc_list[1::2]
print(my_even_list)

# afișează o listă ce conține numerele impare din lista ordonată (folosind slice)

my_odd_list = my_list[1::2]
print(my_odd_list)

my_odd_list = my_asc_list[::2]
print(my_odd_list)

# afișează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).

my_multiplu3_list = my_list[1:10:3]
print(my_multiplu3_list)

my_multiplu_list = my_list[-3::-3]
print(my_multiplu_list)
