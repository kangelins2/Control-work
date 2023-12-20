# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def meow(self):
#         print(f"{self.name}:мяу!")
#
# cat = Cat("Барсик")
# cat2 = Cat("Мурзик")
# cat.meow()
# cat2.meow()


# задание 2
# class student:
#     def __init__(self, full_name, age, course):
#         self.full_name = full_name
#         self.age = age
#         self.course = course
#
#     def info(self):
#         return f"{self.full_name}: {self.age} лет, {self.course} курс."
# sasha = student("Александр", 20, 3)
# print(sasha.info())


# задание 3
# class Field:
#     def __init__(self):
#         self.field = [' '] * 9
#
#     def _check(self, index):
#         return self.field[index] == ' '
#
#     def turn(self, index, symbol):
#         if self._check(index):
#             self.field[index] = symbol
#
#     def print(self):
#         print(self.field[:3])
#         print(self.field[3:6])
#         print(self.field[6:])
#         print()
# field = Field()
# field.print()
# field.turn(3, 'x')
# field.print()
# field.turn(3,'0')
# field.print()


задание 4
class Person:
    def __init__(self, firs_name, last_name, birthday: date):
        self.first_name = firs_name
        self.last_name = last_name
        self.birthday = birthday

    def get_fuii_name(self):
        return f"{self.first_name} {self.last_name}"

    def get
