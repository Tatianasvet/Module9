import random

"""Lambda-функция"""

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda i, j: i == j, first, second)))


"""Замыкание"""

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='utf8') as my_file:
            for data in data_set:
                print(data, file=my_file)
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


"""Метод __call__"""

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
