"""
Напишите скрипт, который прочитает файл 2.txt
И создаст новый файл 2 raint.txt
И точно так же запишет тот же текст, заменив все слова дождь на ДОЖДЬ
(большими буквами)
Учитывая окончания, например дожде -> ДОЖДЕ
"""
# import re
# def main(filename):
#     f = open(filename, 'r', encoding="UTF-8")
#     text = f.read()
#     while True:
#         match = re.search('дожд(ь | е)', text)
#         if match is None:
#             break
#         start, end = match.span()
#         text = text[:start] + text[start: end].upper() + text[end:]
#     print(text)
# main("2.txt")

with open("2.txt", "r", encoding='utf-8') as f:
    text = [
        line.split()
        for line in f.readlines()
    ]
# new_text = []
# for line in text:
#     new_line = []
#     for word in line:
#         if 'дожд' in word.lower():
#             new_line.append(word.upper())
#         else:
#             new_line.append(word)
#     new_text.append(' '.join(new_line))
# print('\n'.join(new_text))


new_text = '\n'.join([
    ' '.join([
        word.upper() if 'дожд' in word.lower() else word
        for word in line
    ])
    for line in text
]) + '\n'
with open("2.txt", "r", encoding='utf-8') as f:
    f.write(new_text)

print('\n'.join(new_text))