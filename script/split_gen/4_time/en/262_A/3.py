def main():
    Y = int(input())
    Y += 2
    if Y % 4 == 0:
        print(Y)
    else:
        while Y % 4 != 0:
            Y += 1
        print(Y)
