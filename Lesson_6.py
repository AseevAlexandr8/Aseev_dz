# file_1 = open('hello.txt', 'r', encoding= 'utf - 8')
# paragrafs = file_1.readline()
# print(paragrafs)
# file_1.close()
# content = file_1.read()
# print(content)
# file_1.close()
# режим доступа к файлу r, r+, w, w+, x, a, a+, t, b

#print(dir(file_1))
#'_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing',
# 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty',
# 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure',
# 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines

# clean_content = content.replace('\n', ' ').replace('\r', ' ')
# print(clean_content)
#
# paragraf = content.splitlines()
# print(paragraf)

# file_1 = open('hello.txt', 'r', encoding= 'utf - 8')
# print(file_1.readline())
# print(file_1.readline())
# file_1.close()
#line = file_1.readline()
# while line:
#     print(line)
#     line = file_1.readline()
# file_1.close()

# for line in file_1:
#     print(line)
# file_1.close()

# with open('hello.txt', 'r', encoding= 'utf - 8') as file_1:
#     for line in file_1:
#         print(line)

# txt = """Пробую записать в файл текст используя метод write(). Если не получится попробую ещё раз! Получилось!!!"""
# with open('write_metod.txt', 'w', encoding='utf-8') as f:
#     f.write(txt)

# txt_lines = ['Теперь пробую записать в файл текст\n',
#              'используя метод writelines()\n'
#              'что будет если w заменить на x'
#              'ничего не получилось(, вернул w']
# with open('writelines_metod.txt', 'w', encoding='utf-8') as f:
#     f.writelines(txt_lines)

# txt = """Пробуем дописать в файл текст.
# Использую метод "а" .
# """
# with open('append_text.txt', 'a', encoding='utf-8') as f:
#     f.write(txt)

# txt ="""Пробую дозаписать в файл текст.
# режим доступа r+
# """
#
# with open('hello.txt', 'r+', encoding='utf-8') as f:
#     f.write(txt)
#
# txt = """Пробую ДОЗАПИСАТЬ текст в файл\n
# Режим ДОСТУПА r+
# """
# with open('hello.txt', 'r+', encoding='utf-8') as f:
#     f.write(txt)

# with open('Hello_2.txt', 'r', encoding='utf-8') as f:
#     print(f.tell())
#     line = f.readline()
#     while line:
#         print(line.strip(), f.tell(), sep='\n')
#         line = f.readline()

# with open('Hello_2.txt', 'r', encoding='utf-8') as f:
#     f.seek(39)
#     print(f.readline().strip())
#     f.seek(142)
#     print(f.readline().strip())

# Сериализация данных



# nums = [random.randint(0, 100) for _ in range(10)]
# nums_as_str = json.dumps(nums)
# # print(nums, type(nums))
# # print(nums_as_str, type(nums_as_str))
#
# # with open('nums.json', 'w', encoding='utf-8') as f:
# #     f.write(nums)
#
# with open('nums.json', 'w', encoding='utf-8') as f:
#     f.write(nums_as_str)
#
# with open('nums.json', 'r', encoding='utf-8') as f:
#     nums_as_str = f.read()
# nums = json.loads(nums_as_str)
# print(nums, type(nums))

# nums = [random.randint(0, 100) for _ in range(10)]
# with open('nums_again.json', 'w', encoding='utf-8') as f:
#     json.dump(nums, f)
#
# with open('nums_again.json', 'r', encoding='utf-8') as f:
#     nums = json.load(f)

# import json
# import random
# import pickle
# from time import perf_counter
#
# nums = [random.random() * 10 ** 6 for _ in range(10 ** 6)]
#
# start = perf_counter()
# with open('random_million.json', 'w', encoding='utf-8') as f:
#     json.dump(nums, f)
# print(f"json saved: {perf_counter() - start}")
#
# start = perf_counter()
# with open('random_million.pickle', 'wb') as f:
#     pickle.dump(nums, f)
# print(f"pickle saved: {perf_counter() - start}")
#
#
# start = perf_counter()
# with open('random_million.json', 'r', encoding='utf-8') as f:
#     nums = json.load(f)
# print(f"json loaded: {perf_counter() - start}, {type(nums)}, {len(nums)}")
#
# start = perf_counter()
# with open('random_million.pickle', 'rb') as f:
#     nums = pickle.load(f)
# print(f"pickle loads: {perf_counter() - start}, {type(nums)}, {len(nums)}")

# import pickle
#
# chunk_size = 256
# with open('random_million.pickle', 'rb') as f:
#     binari_data = bytearray()
#     while True:
#         chunk = f.read(chunk_size)
#         if not chunk:
#             break
#         binari_data.extend(chunk)
#     nums = pickle.loads(binari_data)
# print(f"{type(nums)}, {len(nums)}")

txt = 'привет Python!'
txt_binary = txt.encode(encoding='utf-8')
txt_origin = txt_binary.decode(encoding='utf-8')
print(txt_binary, type(txt_binary))
print(txt_origin, type(txt_origin))
