"""
Сделайте функцию, которая создаст новый список из этого, заменив None на 0
"""

test_lst = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 8, 9],
    [10, 11, 12],
    [13, None, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, None],
]

new_lst = []
for i in test_lst:
    _new_lst = []
    for b in i:
        if b is not None:
            _new_lst.append(b)
        else:
            _new_lst.append(0)
    new_lst.append(_new_lst)

print(new_lst)



