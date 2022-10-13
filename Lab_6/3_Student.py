class Student:
    def __init__(self, fullName, studentCardNumber):
        self.fullName = fullName
        self.id = studentCardNumber

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.id == other.id

    def __str__(self):
        return self.fullName


if __name__ == "__main__":
    DPS = Student('Dmitrieva Polina Stepanovna', '1234')
    KEU = Student('Kulicova Ekaterina Urivna', '9876')
    DPS1 = Student('D P S', '1234')

    print(*{DPS, DPS1, KEU})
