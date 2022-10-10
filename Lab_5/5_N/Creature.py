from Wings import *


class Creature:

    def __init__(self, name, age):
        self.name = name
        self.age = str(age)

    def description(self):
        return "\n".join(["Name: " + self.name,
                          "Age: " + self.age, ''])

    def __str__(self):
        return self.description()


class Mammals(Creature):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Mammals'


class Zebra(Mammals):

    def __init__(self, name, age, white_with_black=True):
        super().__init__(name, age)
        self.white_with_black = str(white_with_black)

    def description(self):
        return "\n".join(["Type: " + self.type,
                          "Name: " + self.name,
                          "Age: " + self.age,
                          "White with black: " + self.white_with_black, ''])


class Dolphin(Mammals):

    def __init__(self, name, age, color='Blue'):
        super().__init__(name, age)
        self.color = color

    def description(self):
        return "\n".join(["Type: " + self.type,
                          "Name: " + self.name,
                          "Age: " + self.age,
                          "Color: " + self.color, ''])


class Bat(Mammals, WebbedWing):
    def __init__(self, name, age):
        super(Bat, self).__init__(name, age)
        self.count = 2


class Insects(Creature):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Creature'


class Bee(Mammals, Wing):
    def __init__(self, name, age):
        super(Bee, self).__init__(name, age)
        self.count = 2


class Butterfly(Mammals, Wing):
    def __init__(self, name, age):
        super(Butterfly, self).__init__(name, age)
        self.count = 4


class Birds(Creature, OverstuffedWing):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Birds'
        self.count = 2


if __name__ == '__main__':

    z = Zebra('Gege', 10)
    print(z)
    d = Dolphin('Bill', 7)
    print(d)
