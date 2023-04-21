import random

from langdetect import detect

# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1

# lst = []
# n = int(input('Print a length of list: '))

# for i in range(n):
#     lst.append(random.randint(0,9))

# print(lst)

# x = int(input('Print a num for search: '))

# count = 0
# for i in range(len(lst)):
#     if lst[i] == x:
#         count += 1
#         i+=1
# print(count)



# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

# lst = []
# n = int(input('Print a length of list: '))

# for i in range(n):
#     lst.append(random.randint(0,9))

# print(lst)

# x = int(input('Print a num for check: '))

# res = lst[0]
# for item in lst:
#     if abs(item-x) < abs(res-x):
#         res = item
# print(res)


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 

# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, 
# Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.





ru_points = {'АВЕИНОРСТ' : 1, 'ДКЛМПУ' : 2, 'БГЁЬЯ' : 3, 'ЙЫ' : 4, 'ЖЗХЦЧ' : 5, 'ШЭЮ' : 8 , 'ФЩЪ' : 10}
eng_points = {'AEIOULNSTR' : 1, 'DG' : 2, 'BCMP' : 3, 'FHVWY' : 4, 'K' : 5, 'X' : 8, 'QZ' : 10 }

user_text = input('Print a word: ')
user_text = list(user_text)
dict_ru = 'АВЕИНОРСТДКЛМПУБГЁЬЯЙЫЖЗХЦЧШЭЮФЩЪ'
dict_eng = 'AEIOULNSTRDGBCMPFHVWYKXQZ'

points = 0

for item in user_text:
    for elem_ru in dict_ru:
        if item == elem_ru:
            lang = 'ru'
        else:
            for item in user_text:
                for elem_eng in dict_eng:
                    if item == elem_eng:
                        lang = 'eng'


if lang == 'ru':
    user_text = list(user_text)
    for item in user_text:
        for key in ru_points:
            if item in key:
                points += ru_points.get(key)   
elif lang == 'eng':
    user_text = list(user_text)
    for item in user_text:
        for key in eng_points:
            if item in key:
                points += eng_points.get(key)   


print(points)