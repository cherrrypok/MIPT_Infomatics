with open("text1.txt", "r") as file:
    for line in file:
        print(' '.join(line.split()))
