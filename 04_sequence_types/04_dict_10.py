"""
10▹ Użytkownik podaje dowolną liczbę N.
Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).

Załóżmy, że użytkownik podał N = 8

Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
k = int(input('Podaj liczbę naturalną N.\n'))
dictionary = {}

for a in range(1,k+1):
   dictionary[a] = (a*a)

print('\n Wynik: ',dictionary)
# for key, value in dictionary.items():
#    print (key, value)