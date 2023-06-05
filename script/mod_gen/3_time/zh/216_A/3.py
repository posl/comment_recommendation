def printX_Y(X, Y):
    if 0 <= Y <= 2:
        print("{}-".format(X))
    elif 3 <= Y <= 6:
        print("{}".format(X))
    elif 7 <= Y <= 9:
        print("{}+".format(X))

if __name__ == '__main__':
    printX_Y()