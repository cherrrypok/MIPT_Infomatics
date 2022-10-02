import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number0', nargs='?', type=int)
    parser.add_argument('-n', '--number', type=int)

    return parser


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error_1. Число не введено")
        sys.exit(1)

    parser = createParser()
    namespace = parser.parse_args()

    if namespace.number0 is not None and namespace.number is not None:
        print("Error_2. Число введено 2 раза")
        sys.exit(2)
    elif namespace.number0 is None:
        number = int(namespace.number)
    else:
        number = int(namespace.number0)

    if number == 0:
        print(0)
    elif number == 1:
        print(1)
    else:
        F1 = 0
        F2 = 1
        Fnow = 10
        for i in range(number - 1):
            Fnow = F1 + F2
            F1 = F2
            F2 = Fnow
        print(Fnow)


