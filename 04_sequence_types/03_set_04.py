"""
4▹ Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

output:

[4, 3, 2, 1]
[14, 13, 12, 11]
[24, 23, 22, 21]
"""
list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
l = len(list)
k = l // 3

list_1 = list[0:k]
list_1.reverse()

list_2 = list[(k):(2*k)]
list_2.reverse()

list_3 = list[(2*k):(3*k)]
list_3.reverse()


print(list_1)
print(list_2)
print(list_3)


