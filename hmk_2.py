#1
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#2
random_list = ['в','"' , '05' , '"' , 'часов', '"' , '17', '"' , 'минут', 'температура', 'воздуха',
'была','"' , '+05', '"' , 'градусов']
test_list = ' ' .join(random_list)
print(test_list)
# не верно
# int = ""
# for i in test_list:
#     int += i
#     int += ""
# print(int)

#3
person_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
'токарь высшего разряда нИКОЛАй', 'директор аэлита']
wief_1 = f'Привет ,{person_list[0]}'
print(wief_1)
wief_2 = f'Привет ,{person_list[1]}'
print(wief_2.capitalize())
wief_3 = f'Привет ,{person_list[2]}'
print(wief_3.capitalize())
wief_4 = f'Привет ,{person_list[3]}'
print(wief_4.title())

#4
price_list = ['42 р, 00 к' , '50 р, 50 к' , '10 р, 95 к' , '15 р, 15 к' , '77 р , 00 к' , '13 р , 00 к' , '51 р, 50 к' , '82 р , 00 к' , '04 р, 05 к' ,'29 р, 05 к']

price_print = f'{price_list}'
print(price_print)

print(id(price_list), price_list)
price_list.sort()
print(id(price_list), price_list)

price_list.reverse()
print(price_list)

price_list = price_list[:5]
print(price_list)