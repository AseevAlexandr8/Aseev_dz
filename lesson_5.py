# import sys
# from time import perf_counter
#
# nums = []
# for num in range(1, 10 ** 6 + 1 , 2):
#     nums.append(num ** 2)
# print(type(nums), sys.getsizeof(nums))
# import sys
#
# nums_gen = (num ** 2 for num in range(1 , 10 ** 6 + 1 , 2))
# print(type(nums_gen), sys.getsizeof(nums_gen))
#
# start = perf_counter()
# num_sum = sum(nums)
# print(num_sum, perf_counter() - start)
#
# start = perf_counter()
# nums_gen_sum = sum(nums_gen)
# print(nums_gen_sum, perf_counter() - start)

from time import perf_counter
#
# start = perf_counter()
# nums = []
# for num in range(1, 10 ** 6 + 1, 2):
#     nums.append(num ** 2)
# num_sum = sum(nums)
# print(num_sum, perf_counter() - start)
#
#
# start = perf_counter()
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# nums_gen_sum = sum(nums_gen)
# print(nums_gen_sum, perf_counter() - start)

# nums = []
# for num in range(1, 10 ** 6 + 1, 2):
#     nums.append(num ** 2)
#
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 +1, 2))
# print(nums[:3])
# print(next(nums_gen), next(nums_gen), next(nums_gen), sep = ', ')
#
# from itertools import islice
# print(*islice(nums_gen, 3))
#
# nums_gen_sum = sum(nums_gen)
# print(nums_gen_sum)
#
# nums_gen_sum = sum(nums_gen)
# print(nums_gen_sum)

# num_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# eng_letter_gen = (chr(code) for code in range(ord('a'), ord('z') + 1))
# print(*eng_letter_gen, sep=' ')

# import sys

# def nums_generator(max_num):
#     for num in range(1, max_num + 1, 2):
#         yield num ** 2
#
#
# nums_gen = nums_generator(10 ** 6)
# print(type(nums_gen), sys.getsizeof(nums_gen))
# print(sum(nums_gen))
#
# nums_100_gen = nums_generator(10 ** 3)
# print(sum(nums_100_gen))
# nums_100000_gen = nums_generator(10 ** 5)
# print(sum(nums_100000_gen))


# def letters_generator(start, end):
#     for code in range(ord(start), ord(end) + 1):
#         yield chr(code)
#
#
# end_uppercese_letter = letters_generator('A', 'Z')
# print(*end_uppercese_letter, sep=' ')

# nums_cube_gen = (num ** 3 for num in range(5 + 1))
# print(type(nums_cube_gen), *nums_cube_gen)
#
#
# nums_cube_gen = (num ** 3 for num in range(5 + 1))
# nums_cube = list(nums_cube_gen)
# print(type(nums_cube_gen), *nums_cube)

# num_cube_c = [num ** 3 for num in range(5 + 1)]
# print(type(num_cube_c), *num_cube_c)
#
# nums_cube = []
# for num in range(5 + 1):
#     nums_cube.append(num ** 3)
# print(nums_cube)

matrix_1 = [
    [1, 4, 3, 3],
    [15, 0, 8, 11],
    ]
matrix_2 = [
    [17, 3, 2, 8],
    [4, 3, 6, 4],
    ]
# matrix_sum = []
# for i in range(len(matrix_1)):
#     row = []
#     for j in range(len(matrix_1[0])):
#         row.append(matrix_1[i][j] + matrix_2[i][j])
#     matrix_sum.append(row)
# print(*matrix_sum, sep='\n')

# matrix_sum_c = [
#     [matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))]
#     for i in range(len(matrix_1))
# ]
# print(matrix_sum_c)
# print(type(matrix_sum_c))

# for m1, m2 in zip(matrix_1, matrix_2):
#     print(f"{matrix_1}, {matrix_2}")

# matrix_sum = [
#     [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
#     for row_1, row_2 in zip(matrix_1, matrix_2)
# ]
# print(matrix_sum)

# weather_data = [
# [-17.5, -18.9, -21.0, -16.1],
# [-9.3, -11.7, -14.3, -15.8],
# ]
# flat_weater_data = []
# for row in weather_data:
#     for el in row:
#         flat_weater_data.append(el)
# print(flat_weater_data)

# flat_weater_data = [el for row in weather_data for el in row]
# print(flat_weater_data)

# flat_weater_data = [el
#                     for row in weather_data
#                     for el in row]
# print(flat_weater_data)
#
# flat_weater_data_2 = [el
#                       for row in weather_data
#                       for el in row
#                       if el > -20]
# print(flat_weater_data_2)

# nums_cube = {num : num ** 3 for num in range(1, 5 + 1)}
# print(nums_cube)

# eng_ru = {'may': 'май', 'june': 'июнь', 'july': 'июль'}
# ru_eng = {val : key for key, val in eng_ru.items()}
# print(ru_eng)

# eng_ru_nums = {'one':'один', 'fist':'один', 'two':'два'}
# ru_eng_nums = {val : key for key, val in eng_ru_nums.items()}
# print(ru_eng_nums)

basket = ['apple', 'samsung', 'apple', 'huawei', 'asus', 'samsung']
# uniqe_basket = [el for el in basket if basket.count(el) == 1]
# print(uniqe_basket)

unique_brands = set()
tmp = set()
for el in basket:
    if el not in tmp:
        unique_brands.add(el)
    else:
        unique_brands.discard(el)
    tmp.add(el)
print(unique_brands)
#
# unique_brand_ord = [el for el in basket if el in unique_brands]
# print(unique_brand_ord)

# pencil_colors = {'red', 'pink', 'green', 'orange'}
#
# chat_1 = {'user_1', 'user_5', 'user_7', 'user_8', 'user_11'}
# chat_2 = {'user_1', 'user_2', 'user_2', 'user_7', 'user_9', 'user_10'}
#
# chat_commons =chat_1.intersection(chat_2)
# print(chat_commons)
#
# chat_1_onli = chat_1 - chat_2
# chat_2_onli = chat_2 - chat_1
# print(chat_1_onli)
# print(chat_2_onli)
#
# both_chats = chat_1.union(chat_2)
# print(both_chats)

# chat_1 = frozenset(('user_1', 'user_5', 'user_7', 'user_8', 'user_11'))
# chat_2 = frozenset(('user_1', 'user_2', 'user_2', 'user_7', 'user_9'))
#
# chat_common = chat_1.intersection(chat_2)
# print(chat_common)

# import random
#
# random_nums = {random.randint(1, 100) for _ in range(10)}
# print(len(random_nums), random_nums)


