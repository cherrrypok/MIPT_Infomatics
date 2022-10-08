class Mother:

    def definition(self):
        return "I'm Mother"

    def __str__(self):
        return self.definition()


class Daughter(Mother):

    def definition(self):
        return "I'm Daughter"


if __name__ == "__main__":
    m = Mother()
    print(m)
    d = Daughter()
    print(d)