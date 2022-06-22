#1
# with open('adress.txt', 'r', encoding='utf-8') as f:
#     content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
#     for i in content:
#         print(i)

#3
# with open('users.csv', 'r', encoding='UTF-8') as file_users:
#     for line_u in file_users:
#         print(line_u)
#
# with open('hobby.csv', 'r', encoding='UTF-8') as file_hobby:
#     for line_h in file_hobby:
#         print(line_h)
#
# for user, hobby in zip(line_u, line_h):
#     print(f"{user}, {hobby}")

from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='UTF-8') as users:
    with open('hobby.csv', 'r', encoding='UTF-8') as hobby:
        all_list = zip_longest((" ".join(us.split(",")) for us in users, hobby, fillvalue=None)
        my_dict = {str(el[0]).strip(): (str(el[1]).strip()) if el[0] else exit(1) for el in all_list}

        with open('dict_n_h.json', 'w', encoding='UTF-8') as f:
            dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)
