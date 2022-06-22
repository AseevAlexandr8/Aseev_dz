# winter_months = ['декабрь', 'январь', 'февраль']
# print(type(winter_months) == list)
# print(isinstance(winter_months , list))
# print(type(winter_months))
# print(dir(winter_months))
# #['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# winter_months.append(123456789)
# print(winter_months)
# winter_months.extend([1 , 2 , 3 , 789])
# print(winter_months)
#
#
# winter_months.append([1 , 2])
# print(winter_months)


# winter_months = ['декабрь', 'январь', 'февраль']
# winter_months_2 = winter_months.pop()
# print(winter_months_2)

# winter_months = ['декабрь', 'январь', 'февраль']
# cur_winter_monts = winter_months.pop(2)
# print(cur_winter_monts)
# print(winter_months)

# basket_prices = [3000.0, 1580.0, 3000.0, 2785.8]
# print(basket_prices.count(3000.0))
# print(basket_prices.index(2785.8))

# winter_months = ['декабрь', 'февраль']
# print(winter_months)
# winter_months.insert(0 , 'ноябрь')
# print(winter_months)

# winter_months = ['декабрь', 'январь', 'январь', 'январь', 'февраль']
# # while winter_months.count('январь') > 1 :
# #     winter_months.remove('январь')
# #     print(winter_months)
# winter_months.remove('январь')
# print(winter_months)

# winter_months = ['декабрь', 'январь', 'февраль']
# print(id(winter_months) , winter_months)
# # winter_months.reverse()
# # print(id(winter_months) , winter_months)
# winter_months_reverse = list(reversed(winter_months))
# print(id(winter_months_reverse) , winter_months_reverse)

# year_months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн',
# 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
# # fist_qartal =year_months [0 : 3 ]
# # print(fist_qartal)
# # second_qartal = year_months [3 : 7]
# # print(second_qartal)
# # out_year = year_months [8 :]
# # print(out_year)
# # year_list = year_months [0 : 100]
# # print(year_list)
# odd_mounts = year_months [::2]
# print(odd_mounts)
# second_odd_mounts = year_months [1::3]
# print(second_odd_mounts)
# revers_mounts = year_months[::-1]
# print(id(year_months) , year_months , id(revers_mounts) , revers_mounts)

# winter_months = ['декабрь', 'январь', 'февраль']
# print(id(winter_months) , winter_months)
# winter_months.sort()
# print(id(winter_months) , winter_months)
#
# winter_months = ['декабрь', 'январь', 'февраль']
# print(id(winter_months) , type(winter_months),winter_months)
# winter_months_s = sorted(winter_months , reverse= True)
# print(id(winter_months_s) , type(winter_months_s) , winter_months_s)
import sys

# some_list = ['hello', True, 'word', 1, 2.2]
# print(type(some_list) , sys.getsizeof(some_list) , some_list)
# some_list_2 = ('hello', True, 'word', 1, 2.2)
# print(type(some_list_2) , sys.getsizeof(some_list_2) , some_list_2)

# some_tuple = ('hello', True, 'word', 1, 2.2)
# # some_tuple_2 = 'hello', True, 'word', 1, 2.2
# # print(some_tuple)
# # print(some_tuple_2)
# print(dir(some_tuple))
#
# some_list = ['hello', True, 'word', 1, 2.2]
# some_list[0] = 'hi man'
# print(some_list)
# some_list[3] ='123456789'
# print(some_list)

# some_list = ('hello', True, 'word', 1, 2.2)
# some_list[2] = '123'
# print(some_list)

# a = [['hello'], 10 , 123 , 1.05]
# b = a
# print(id(a) , a , id(b) , b)
# b[0] = 'hi'
# print(id(a) ,a , id(b) , b)

# a = [1 , 2 , 3 , 4.0]
# print(id(a) , a)
# b = a[:]
# print(id(b) , b)
# print(id(a[1]) , id(b[1]))
# b[1] = 'hi'
# print(a , b)
# print(id(a[1]) , id(b[1]))

# a = [1 , 2 , 3 , 4.0]
# b = a.copy()
# print(id(a) , a , id(b) , b)
# b[2] = 'man'
# print(a , b)
from copy import copy
# a = [1 , 2 , 3 , 4.0]
# b = copy(a)
# print(id(a) , a , id(b) , b)
# b[0] = '123'
# print(a ,b)
#
# from copy import deepcopy
# a = [1 , 2 , 3 , 4.0 , 'hihihihi']
# b = deepcopy(a)
# print(id(a) , a , id(b) , b)
# print(id(a[0]) , id(b[0]))
# b[0] = 'python'
# print(a ,b)
# print(id(a[0]) , id(b[0]))

# message = 'привет всем'
# print(message[:message.index(' ')])
# print(ord(message[0]))
# print(chr(ord(message[0]) - 1))
# print(message[::-1])

# raw_message = ['python' , 'современный' , 'язык']
# message = ' '
# for item in raw_message:
#     message += item
#     message += ' '
# print(message)

# new_list = ['один' , 'два' , 'три' , 'четыре' , 'пять' , 'шесть' , 'семь']
# word = ''
# for i in new_list:
#     word += i
#     word += ' '
# print(word)
# new_list = ['один' , 'два' , 'три' , 'четыре' , 'пять' , 'шесть' , 'семь']
# word = ' '.join(new_list)
# print(word)

# name = 'Alexandr'
# age = 2023
# message = 'Уважаемый ' + name + '! Поздравляем c ' + str(age) + 'годом !'
# print(message)
#
# name, year = 'Иван', 2021
# greeting = 'Уважаемый, ' + name + '! Поздравляем с ' + str(year) + ' годом!'
# print(greeting)
#
# name_1 , year = 'Alexandr' , 2023
# # word = 'Уважаемый ' +name+ ' поздравляем с наступающим ' +str(year)
# # print(word)
# # message = 'Уважаемый %s ! Поздравляем с наступающим %d !' % (name_1 , year)
# # print(message)
# message = 'Уважаемый , {} ! С наступающим {} !' .format( name_1 , year )
# print(message)
# # name, year = 'Иван', 2021
# # # greeting = 'Уважаемый, ' + name + '! Поздравляем с ' + str(year) + ' годом!'
# # # print(greeting)
# # # greeting = 'Уважаемый, %s! Поздравляем с %d годом!' % (name, year)
# # print(greeting)

# name, year, month, money = 'Борис', 2022, 3, 1789.47689
# # mes = '{0} ! Сегодны {1} месяц {2} года'.format(name , month , year )
# # print(mes)
# # mes_2 = '{2:^15}! Сегодня {1:02d} месяц {0} года.'.format(year ,month ,name)
# # print(mes_2)
# # mes_3 = f'{name:>15} ! На счете {money:.1f}'.format(name=name , money=money)
# # print(mes_3)
# met = f'уважаемый {name} с наступающим {year} !'
# print(met)
# met_2 = f'{name:^15} !Сегодня {month:02d} месяц {year} года !'
# print(met_2)
# met_3 = f'{name:^15} ! На счете {money:.2f}'
# print(met_3)

# url = '“https://geekbrains.ru/teacher/lessons/79615”'
# url_pers = url.split('/')
# print(url_pers)
# _t_proyocol, _, domain, *reours_adress = url.split('/')
# t_protocol = _t_proyocol[:-1]
# print(t_protocol , domain , reours_adress)
# _t_protocol, _,domain , *resours_adress = url.split('/')[:3]
# print(url)

# raw_url = ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']
# url = '/'.join(raw_url)
# print(url)
# raw_url_2 = ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']
# url_2 = '/'.join(raw_url_2)
# print(url_2)
# msg = 'Товаров в корзмне : 5'
# print(msg.upper())
# print(msg.lower())

# msg = 'тОВАров в коРЗИНЕ: 5. стоимость: 4789,5 руб.'
# print(msg.title())
# print(msg.capitalize())
# msg = 'а роза упала на лапу Азора'
# print(msg[::-1])
# # print(msg.__reversed__())