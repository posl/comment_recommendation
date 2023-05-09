def printSign(X, Y):
    if 0 <= Y and Y <= 2:
        print(str(X) + "-")
    elif 3 <= Y and Y <= 6:
        print(str(X))
    elif 7 <= Y and Y <= 9:
        print(str(X) + "+")

if __name__ == '__main__':
    printSign()