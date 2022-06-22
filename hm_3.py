#1
num_list = {
    'zero': "ноль",
    'one': "один",
    'two': "два",
    'thee': "три",
    'four': "четыре",
    'five': "пять",
    'six': "шесть",
    'seven': "семь",
    'eit': "восемь",
    'nine': "девять",
    'ten': "десять"
}


def num_translate(i):
    return num_list.get(i)


print(num_translate(input('впишите число :')))


#3
person_list = {
    "И": ["Иван", "Илья"],
    "М": ["Мария"],
    "П": ["Петр"]
}


def thesaurus(a):
    return person_list.get(a)


print(thesaurus(input('впишите ключ: ')))

#5
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

for noun, adv , adj in zip(nouns, adverbs, adjectives):
    print(f"{noun}, {adv}, {adj}")
