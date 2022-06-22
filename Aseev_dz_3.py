# a = 6
# print(a)
# print(id(a))
#
# a = '6'
# print(a)
# print(id(a))
#
# a = 6.0
# print(a)
# print(id(a))
#
# z = input('введите имя: ')
# print('здравствуйте' , z, '!')
# print(id(z))


# print(5 ** 5)
# x = 4
# y = x **15
# print(y)

# print(5/2)
# print(5//2)
# print(5%2)

# a = 17 % 5
# b = 5 % 5
# c = 3 % 5
# d = 0 % 5
# print(a)
# print(b)
# print(c)
# print(d)

# rows = 128
#
# adress = 147
# adress_2 = adress % rows
# print(adress_2)
#
# adress = 100
# adress_2 = adress % rows
# print(adress_2)
#
# adress = 128
# adress_2 = adress % rows
# print(adress_2)
#
# adress = 600
# adress_2 = adress % rows
# print(adress_2)


# print(True and True)
# print(True and False)
# print(False and True)
#
# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)

# print(not True)
# print(not False)
#
# print(True and True is not True)

# age = 25
# gender = 'M'
# its_gender = gender == 'F' and age>20
# print(its_gender)

# room_number = 64
# cleaning = room_number and room_number // 10 > 4 or room_number % 10 == 2
# print(cleaning) # True
#
# room_number = 78
# do_cleaning = room_number and room_number // 10 > 7 or room_number % 10 == 3
# print(do_cleaning) # False
#
# room_number = 73
# do_cleaning = room_number and room_number // 10 > 7 or room_number % 10 == 3
# print(do_cleaning) # True


# number = 73
# if not number % 2 :
#     print('чётное число')
# else:
#     print('нечётное число')


# years_monts = ['январь' , 'февраль' , 'март' , 'апрель' , 'май']
# print(years_monts)
# print(years_monts[3])
#
# years_monts[0] = 'декабрь'
# print(years_monts)
#
# years_monts.append('июнь123')
# print(years_monts)

# day_sales = [15, 26, 54, 12, 47 , 55 , 71 , 61]
# idx = 0
# total_sales = 0
# while idx < len(day_sales) :
#     total_sales = total_sales + day_sales[idx]
#     idx = idx +1
# price_product = total_sales / len(day_sales)
# print(price_product)



# work_day = [150 , 143 , 320 , 72]
# idx = 0
# total_work = 0
# while idx < len(work_day) :
#     total_work =total_work + work_day[idx]
#     idx += 1
# day_work_total = total_work / len(work_day)
# print(day_work_total)


# day_sales = [15, 26, 54, 12, 47 , 55 , 71 , 61]
# total_sales = 0
# for total_day in day_sales :
#     total_sales += total_day
# price_product = total_sales / len(day_sales)
# print(price_product)
#
#
#
# a = [150 , 143 , 320 , 72 , 15, 26, 54, 12, 47 , 55 , 71 , 61]
# b = 0
# for c in a :
#     b += c
# i = b / len(a)
# print(i)

# day_sales = [1589, 2687, 5478, 1236]
# discount = 10
# for idx in range(len(day_sales)):
#     day_sales[idx] *= (100 - discount) / 100
# print(day_sales)
#
# for idx, item in enumerate(day_sales, start=1):
#     print('товар №' , idx , '-' , item)

# num = 457
# tree_num = 0 < num // 100 <= 9
# print(tree_num)
#
# ten = num % 100 // 10
# print(ten)

# трёхзначное и средняя цифра 2
# num = 924
# two_num = 0 < num // 100 <=9
# print(two_num)
# two = num % 100 // 10
# print(two)

# num_list =[i for i in range(1 , 101)]
# print(num_list)
# for ind in enumerate(num_list):
#     print(ind)

# val = int(input('введите число :'))
# val = 0
# if val % 10 == 1:
#     print('процент')
# elif val % 10 == 2:
#     print('процента')
# elif val % 10 == 3:
#     print('процента')
# elif val % 10 == 4:
#     print('процента')
# elif val % 10 == 5:
#     print('процентов')
# elif val % 10 == 6:
#     print('процентов')
# elif val % 10 == 7:
#     print('процентов')
# elif val % 10 == 8:
#     print('процентов')
# elif val % 10 == 9:
#     print('процентов')
# elif val % 10 == 10:
#     print('процентов')
# for ind , val in enumerate(num_list):
#     print(ind , val)

    #
    # if num % 10 == 1:
    #     word = 'процент'
    # elif num % 10 == 2:
    #     word = 'процента'
    # elif num % 10 == 3:
    #     word = 'процента'
    # elif num % 10 == 4:
    #     word = 'процента'
    # elif num % 10 == 5:
    #     word = 'процентов'
    # elif num % 10 == 6:
    #     word = 'процентов'
    # elif num % 10 == 7:
    #     word = 'процентов'
    # elif num % 10 == 8:
    #     word = 'процентов'
    # elif num % 10 == 9:
    #     word = 'процентов'
    # elif num % 10 == 10:
    #     word = 'процентов'


# day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]
# for idx, item in enumerate(day_sales, start=1):
# print('товар №', idx, '-', item)

a = ("Процент")
b = ("Процента")
c = ("Процентов")
i = input("Введите сколько у вас HP:")
numbs = {11,12,13,14}
for i in range(100):
    i = i + 1
    if i in numbs:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif i % 10 > 1 and i % 10 <5:
        print(i, "процента")
    else:
        print(i, "процентов")