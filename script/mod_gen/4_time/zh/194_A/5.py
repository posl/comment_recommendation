def icecreamType(A, B):
    if (A+B) < 15:
        print(4)
    elif (A+B) >= 15 and B >= 8:
        print(1)
    elif (A+B) >= 10 and B >= 3:
        print(2)
    elif (A+B) >= 3:
        print(3)

if __name__ == '__main__':
    icecreamType()