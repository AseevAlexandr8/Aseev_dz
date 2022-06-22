# # def url_parse(url):
# #     """parses code
# #     and parsesed codes
# #     url adress
# #     """
# #     _t_protocol, domain, *resours_adress = url.strip('/').split('/')
# #     t_protocol = _t_protocol[:-1]
# #     return t_protocol, domain, resours_adress
#
#
# # print(help(url_parse))
#
# # url = 'https://geekbrains.ru/teacher/lessons/7961'
# # _t_protocol, _, domain, *resours_adress= url.strip('/').split('/')
# # t_protocol = _t_protocol[:-1]
# # print(t_protocol, domain, resours_adress)
# #
# # url = 'https://www.citilink.ru/catalog/mobile/notebooks/1202859/'
# # _t_protocol , domain, *resours_adress = url.strip('/').split('/')
# # t_protocol = _t_protocol[:-1]
# # print(t_protocol, domain, resours_adress)
# # #
# # url = 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/'
# # _t_protocol, domain, *resours_adress = url.split('/')
# # t_protocol = _t_protocol[:-1]
# # print(t_protocol, domain, resours_adress)
#
# # url_1 = 'https://geekbrains.ru/teacher/lessons/7961'
# # url_1_parser = url_parse(url_1)
# # print(url_1_parser)
# #
# # url_2 = 'https://www.citilink.ru/catalog/mobile/notebooks/1202859/'
# # print(url_parse(url_2))
# #
# # print(url_parse('https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/'))
#
# # print(type(url_parse), id(url_parse))
# # new_url_parse = url_parse
# # print(type(new_url_parse), id(new_url_parse))
# # print(new_url_parse('https://cloud.mail.ru/home/'))
#
# # nums = ['1578.4', '892.4', '354.1', '871.5']
# # summ = 0
# # for num in nums:
# #     summ +=float(num)
# # print(summ)
# #
# # nums = [1578.4, 892.4, 354.1, 871.5]
# # print(sum(nums))
# #
# # nums = ['1578.4', '892.4', '354.1', '871.5']
# # print(sum(map(float, nums)))
#
# # urls = ['https://geekbrains.ru/teacher/lessons/7961',
# # 'https://www.citilink.ru/catalog/mobile/notebooks/1202859/',
# # 'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/']
# # urls_parsed = map(url_parse, urls)
# # print(*urls_parsed,sep='\n')
#
#
# # def say_hello():
# #     print(name)
# #
# #
# # name = 'Alexandr'
# # say_hello()
#
#
# # def hallo():
# #     name = 'Alexandr'
# #     print(name)
# #
# #
# # name = 'ivan'
# # print(name)
# # hallo()
#
#
# # def say_hello_wrapper():
# #     # name = 'Ivan'
# #
# #
# #     def say_hello():
# #         print(name)
# #
# #
# #     say_hello()
# #
# #
# # name = 'Alexandr'
# # say_hello_wrapper()
#
#
# # def say_hello():
# #     name = 'Ivan'
# #     print(name)
# #
# #
# # name = 'Alexandr'
# # say_hello()
# # print(name)
#
#
# # def say_hello():
# #     global name
# #     name = 'Ivan'
# #     print(name)
# #
# #
# # name = 'Alexandr'
# # print(name)
# # say_hello()
# # print(name)
#
# # user_1 = ['Иванов', 'Иван', 'Иванович', 25]
# # user_2 = ['Петров', 'Петр', 'Петрович', 28]
# #
# #
# # def user_info(user):
# #     print(f'{user[0]}, {user[1]}, {user[3]}, лет')
#
#
# # user_info(user_1)
# # user_info(user_2)
#
# # user_3 = {
# #     'fist_name': 'Иванов',
# #     'last_name': 'Иван',
# #     'patronomic': 'Иванович',
# #     'age': 25
# # }
# #
# # print(user_3['last_name'])
# # print(user_3['age'])
# #
# #
# # def user_info_adv(user):
# #     print(f"{user['fist_name']} {user['last_name']}, {user['age']} лет")
# #
# #
# # user_info_adv(user_3)
#
# # user_4 = {
# #     0 : 'Иванов',
# #     1 : 'Иван',
# #     2 : 'Иванович',
# #     3 : 25
# # }
# # print(user_4[1], user_4[0], user_4[3])
#
# # user_5 = {'first_name': 'Иван', 'last_name': 'Иванов', 'age': 25}
# # print(user_5.get('adress','задайте адрес'))
#
# # user_6 = {'first_name': 'Сергей', 'last_name': 'Сергеев', 'age': 25}
# # print(user_6.setdefault('адрес', 'Россия'))
# # print(user_6)
#
# # user_7 = {'first_name': 'Александр', 'last_name': 'Александров', 'age': 30}
# # print(user_7.setdefault('age', 20))
# # print(user_7)
#
# # user_7 = {'fist_name' : 'Дмитрий'}
# # user_7['last_name'] = 'Петров'
# # user_7['age'] = 30
# # print(user_7)
#
# # address = {'street': 'Невский проспект', 'house': 15}
# # user_8 = {'fist_name':'Ivanov', 'last_name': 'Ivan'}
# # user_8.update(address)
# # print(user_8)
#
# # user_9 = {'first_name': 'Роман', 'last_name': 'Григорьев', 'street': 'Ленина'}
# # some_pare = user_9.popitem()
# # print(some_pare)
# # print(user_9)
# #
# # user_10 = {'first_name': 'Егор', 'last_name': 'Родионов'}
# # use_pop = user_10.pop('first_name')
# # print(user_10)
# # print(use_pop)
#
# # dns = {
# # 'mail.ru': '94.100.180.201',
# # 'geekbrains.ru': '178.248.232.209',
# # 'amazon.com': '205.251.242.103'
# }
# # for item in dns:
# #     print(item)
# #
# # print('mail.ru' in dns)
# # print('avito.ru' in dns)
#
# # for key, val in dns.items():
# #     print(f"{key} = {val}")
#
# # for item in dns.items():
# #     print(item, end = '->')
# #     key, val = item
# #     print(f"{key}:{val}")
#
# # for val in dns.values():
# #     print(val)
# # for key in dns.keys():
# #     print(key)
#
# # def my_sum(args):
# #     return sum(args)
# #
# #
# # print(my_sum([10, 25 , 99]))
# # print(my_sum(15, 25))
#
# # def my_sum_adv(*args):
# #     print(type(args))
# #     return sum(args)
# #
# #
# # print(my_sum_adv(77, 151, 1))
# # print(my_sum_adv(*[1, 4, 5]))
#
#
# # def box_area(w, h):
# #         return w * h
# #
# #
# # print(box_area(5 , 4))
# # print(box_area(125 , 95))
#
#
# # def box_arena(w , h, scale=1.0):
# #     return w * h * scale ** 2
# #
# #
# # print(box_arena(3 , 5))
# # print(box_arena(5 , 7 ,0.01))
#
#
# # def box_show(w , h , unit = 'м', lang = 'ru'):
# #     if lang == 'ru':
# #         print(f'ширина {w} {unit}, высота {h} {unit}')
# #     else:
# #         print(f'widch {w} {unit}, height {h} {unit}')
#
#
# # box_show(15 , 10)
# # box_show(5 , 10 , 'см')
# # box_show(h=5 , w=10)
# # box_show(5 , 15 , 'м' ,lang='en')
# # box_show(h=10 , w=5)
# # box_show(5 , 10 , lang='en')
# # box_show(h=5 , w=10)
#
#
# # def box_show(w , h , unit='м' , lang='ru' , **kwargs):
# #     print(f'kwargs: {kwargs}')
# #     if lang == 'ru':
# #         print(f'ширина {w} {unit} , высота {h} {unit}')
# #     else:
# #         print(f'widch {w} {unit} , height {h} {unit}')
# #
# #
# # box_show(5 , 10 ,lang='en' , color = 'red')
#
#
# # def show_user(name , *args , **kwargs):
# #     print(f'пользователь {name}')
# #     print(f'args {args}')
# #     print(f'kwargs {kwargs}')
# #
# #
# # # show_user('Alexandr' , 'Aseev' , age= 26)
# #
# # user_full_name = ('Ivan' , 'Ivanov')
# # user_add_info = {'height': 180, 'age': 25}
# #
# # show_user(*user_full_name , **user_add_info)
#
# from random import randrange
#
#
# # product = ['яблоко', 'груша', 'банан', 'авокадо']
# # random_ind = randrange(len(product))
# # bonus = product[random_ind]
# # print(bonus)
#
# from random import choice
#
# # product = ['яблоко', 'груша', 'банан', 'авокадо']
# # bonus = choice(product)
# # print(bonus)
#
#
# # def accepter(el):
# #     return el.lower().startswith('i')
# #
# #
# # products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# # products_sample = filter(accepter , products)
# # print(type(products_sample))
# # print(*products_sample)
#
# # nums = ['0', 'Samsung Galaxy', '15.5', '18,1', 'iPhone', '748', 'HelloWord']
# # int_nums = list(filter(str.isalpha , nums))
# # print(int_nums)
#
# # products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# # products_sumple = filter(lambda x: x.lower().startswith('i'), products)
# # print(*products_sumple)
#
# # prices = ['1578.4', '892.4', '354.1', '871.5']
# # prices_float = tuple(map(float , prices))
# # print(type(prices[0]) , type(prices_float[0]) , prices_float)
#
# # discount = 8
# # prices = ['1578.4', '892.4', '354.1', '871.5']
# # prices_discount = map(
# #     lambda x: round(float(x) * (100 - discount) / 100 , 2),
# #     prices
# # )
# # print(*prices_discount)
#
# prices = ['15,78.4', '892.4', '354.1 rub', '871.5', '47,1']
# prices_float = map(float,
#                    filter(lambda x: x.replace('.', '', 1).isdigit(), prices))
# print(prices_float)
# из методичкb
# prices = ['15,78.4', '892.4', '354.1 rub', '871.5', '47,1']
# prices_float = map(float,
#                    filter(lambda x: x.replace('.', '', 1).isdigit(), prices))
# print(*prices_float)
# # прописал
# prices = ['15,78.4', '892.4', '354.1 rub', '871.5', '47,1']
# prices_float = map(float,
#                    filter(lambda x: x.replace('.', '', 1).isdigit(), prices))
# print(*prices_float)


# user_names = ['Иван', 'Петр', 'Ольга', 'Сергей']
# user_logins = ['ivan', 'petr', 'olga', 'sergey']
# user_roles = ['user', 'staff', 'admin', 'user']
# # for i in range(len(user_names)):
# #     print(f'{user_names[i]}, {user_logins[i]}', user_roles[i])
#
# for name, logins, role in zip(user_names, user_logins, user_roles):
#     print(f'{name}, {logins}, {role}')
