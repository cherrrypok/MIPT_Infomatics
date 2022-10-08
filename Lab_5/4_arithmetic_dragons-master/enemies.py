# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


def is_simple(number):
    if number == 1:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def multipliers(number):
    n = number
    multipliers = []
    for i in range(2, number // 2 + 1):
        while n % i == 0:
            if number % i == 0 and is_simple(i):
                n = n // i
                multipliers.append(i)
    if is_simple(number):
        multipliers.append(number)
    return multipliers



class Monster(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Monster):
    def __init__(self):
        self._health = 50
        self._attack = 10
        self._color = 'Зеленый'
        self._type = 'Дракон'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Monster):
    def __init__(self):
        self._health = 50
        self._attack = 15
        self._color = 'Красный'
        self._type = 'Дракон'


    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        if x < y:
            x, y = y, x
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Monster):
    def __init__(self):
        self._health = 50
        self._attack = 20
        self._color = 'Черный'
        self._type = 'Дракон'


    def question(self):
        x = randint(1, 10)
        y = randint(1, 10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class TrollRandom(Monster):
    def __init__(self):
        self._health = 100
        self._attack = 5
        self._color = 'Рандом'
        self._type = 'Троль'


    def question(self):
        x = randint(1, 5)
        self.__quest = 'отгадайте число от 1 до 5, которое загадал Рандом троль'
        self.set_answer(x)
        return self.__quest


class TrollSimple(Monster):
    def __init__(self):
        self._health = 100
        self._attack = 30
        self._color = 'Простой'
        self._type = 'Троль'


    def question(self):
        x = randint(1, 100)
        self.__quest = str(x) + ' напишите 1, если число простое и 0,в противном случае'
        if is_simple(x):
            self.set_answer(1)
        else:
            self.set_answer(0)
        return self.__quest


class TrollMultipliers(Monster):
    def __init__(self):
        self._health = 50
        self._attack = 10
        self._color = 'Множительный'
        self._type = 'Троль'


    def question(self):
        x = randint(1, 100)
        self.__quest = str(x) + ' перечислите простые множители числа, из которого оно состоит, без пробелов'
        self.set_answer(int(''.join([str(i) for i in multipliers(x)])))
        return self.__quest
    pass


enemy_types = [GreenDragon, RedDragon, BlackDragon, TrollRandom, TrollSimple, TrollMultipliers]
