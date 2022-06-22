#1

duration = int(input('введите число :'))
if duration <= 60:
    print(duration , 'сек')
elif duration <= 3600 :
    print( duration //60 , 'мин' , duration % 60 , 'сек')
elif duration <= 86400 :
    print(duration // 3600 , 'час' , duration % 3600 , 'мин' , duration %3600 % 60 , 'сек')
# переделать
else:
    print(duration // 86400 , 'дн' , duration % 86400 % 3600 , 'час' , duration % 3600 % 60 , 'мин' , duration % 3600 % 60 , 'сек')


#2

a = [b for b in range(1 , 1000 , 2)]
print(a)
kub_list = [a * a * a for a in a]
print(kub_list)
all_sum = 0

for i in kub_list:
    print(i)
# idx = num // 100 + num // 100 / 100 + num // 100 // 100 // 10 примерно набрасал решение чтобы не забыть
# подсмотрел решение
for ind , val in enumerate(kub_list):
    sum_num = 0
    while val > 0 :
        sum_num += val % 10
        val //= 10
    if sum_num % 7 == 0 :
        all_sum += kub_list[ind]
print(all_sum)

# for b in kub_list:
#     add_kub_list.append(b + 17)
# all_sum = 0
# списал, не понимаю как это работает

# 3
for nums in range(1 , 101):
    if nums % 10 == 1:
        print(nums , 'процент')
    elif nums % 10 == 2:
        print(nums , 'процента')
    elif nums % 10 == 3:
        print(nums , 'процента')
    elif nums % 10 == 4:
        print(nums , 'процента')
    else:
        print(nums , 'процентов')

