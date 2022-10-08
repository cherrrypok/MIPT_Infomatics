class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = str(age)

    def description(self):
        return "\n".join(["Name: " + self.name,
                          "Age: " + self.age, ''])

    def __str__(self):
        return self.description()


class Zebra(Animal):

    def __init__(self, name, age, white_with_black=True):
        super().__init__(name, age)
        self.type = 'Zebra'
        self.white_with_black = str(white_with_black)

    def description(self):
        return "\n".join(["Type: " + self.type,
                          "Name: " + self.name,
                          "Age: " + self.age,
                          "White with black: " + self.white_with_black, ''])


class Dolphin(Animal):

    def __init__(self, name, age, color='Blue'):
        super().__init__(name, age)
        self.type = 'Dolphin'
        self.color = color

    def description(self):
        return "\n".join(["Type: " + self.type,
                          "Name: " + self.name,
                          "Age: " + self.age,
                          "Color: " + self.color, ''])


if __name__ == '__main__':

    z = Zebra('Gege', 10)
    print(z)
    d = Dolphin('Bill', 7)
    print(d)
