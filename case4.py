import re
spisok = []
list_1 = []
list_2 = []

def first(list_1, list_2):
    with open('input.txt', 'r+') as file:
        lines = file.readlines()
        for j in lines:
            line = j[:-1]
            line += ' '
            spisok.append(line)
        # print(spisok)  # 1-2 пункты задания
        for i in spisok:
            list_1.append(re.split(' ', i[:-1]))
            list_2.append(list(filter(None,  re.split('\W', i))))

    return list_1, list_2  # со знаками препинания, чисто слова и ни чего больше
first(list_1, list_2)

list_of_words = []
for j in list_2:
    for a in j:
        list_of_words.append(a)
print(list_of_words)         # список слов по порядку
words = set(list_of_words)   # не повторяющиеся слова
print(words)
first_words = []                 # стартовые слова ,заглавные
for q in words:
    if q[0] == q[0].upper():
        first_words.append(q)
print(first_words)s
for n in range(len(list_of_words)):
    for ken in first_words:
        if list_of_words[n] == ken:
            pass
