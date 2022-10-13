class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def string(cls, str):
        x, y, z = [int(i) for i in str.split(',')]
        return cls(x, y, z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) != Vector:
            return Vector(self.x * other, self.y * other, self.z * other)
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        if type(other) != Vector:
            return Vector(self.x / other, self.y / other, self.z / other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    @staticmethod
    def greatest_distance(*args):
        N = args[0]
        max_vector = Vector(0, 0, 0)
        max_len = 0
        for i in range(N):
            input_vector = Vector(args[i * 3 + 1], args[i * 3 + 2], args[i * 3 + 3])
            if abs(input_vector) > max_len:
                max_len = abs(input_vector)
                max_vector = input_vector
        return max_vector

    @staticmethod
    def center_of_mass(*args):
        N = args[0]
        summ = Vector(0, 0, 0)
        for i in range(N):
            input_vector = Vector(args[i * 3 + 1], args[i * 3 + 2], args[i * 3 + 3])
            summ = summ + input_vector
        return summ / N


if __name__ == "__main__":
    a = Vector(1, 2, 3)
    b = Vector.string('2, 4, -5')
    print('\nalgebraic operations \n')
    print(a + b)  # (3, 6, -2)
    print(a - b)  # (-1, -2, 8)
    print(a * b)  # (2, 8, -15)
    print(a, b)
    print(abs(a))
    print(a * 4)
    print('\nstaticmethod\n')
    print(Vector.greatest_distance(3, 1, 2, 3, 0, 0, 0, 2, 3, 4))
