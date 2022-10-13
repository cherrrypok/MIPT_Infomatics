class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        if self == other:
            return abs(self)
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        num = abs(other) ** 2
        return Complex((self.re * other.re + self.im * other.im) / num, (-1 * self.re * other.im + self.im * other.re) / num)

    def __str__(self):
        if self.im < 0:
            return '{} - {}i'.format(self.re, abs(self.im))
        return '{} + {}i'.format(self.re, self.im)

    def __repr__(self):
        return 'Complex({}, {})'.format(self.re, self.im)


if __name__ == "__main__":
    a = Complex(1, 3)
    b = Complex(-1, -6)
    print(a + b)  # - 3i
    print(a - b)  # 2 - 9i
    print(a * b)  # 17 - 9i
    print(a / b)  # -19/37 + 3i/37
