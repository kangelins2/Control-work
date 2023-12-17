"""
Напишите скрипт, который прочитает файл 2.txt
И создаст новый файл 2 raint.txt
И точно так же запишет тот же текст, заменив все слова дождь на ДОЖДЬ
(большими буквами)
Учитывая окончания, например дожде -> ДОЖДЕ
"""
import re
def main(filename):
    f = open(filename, 'r', encoding="UTF-8")
    text = f.read()
    while True:
        match = re.search('дожд(ь | е)', text)
        if match is None:
            break
        start, end = match.span()
        text = text[:start] + text[start: end].upper() + text[end:]
    print(text)
main("2.txt")
