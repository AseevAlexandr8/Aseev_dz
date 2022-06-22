import sys


# def nums_generator(max_num):
#     for num in range(1, max_num + 1, 2):
#         yield num ** 2

#1, 2
# odd_gen = (num for num in range(1, 100, 2))
# print(next(odd_gen))
# print(next(odd_gen))
# print(*odd_gen)

# matrix_sum = [
# [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
# for row_1, row_2 in zip(matrix_1, matrix_2)
# ]

#3
from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(result))
print(*islice(result, 9))
print(list(islice(result, 3)))


#4
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [src[num] for num in range(1, len(src)) if src[num] > src[num - 1]]
# print(result)

#5
# src_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# my_dict = {i: 0 for i in src_list}
# for i in src_list:
#     my_dict[i] +=1
# print([i for i in my_dict if my_dict[i] == 1] )
