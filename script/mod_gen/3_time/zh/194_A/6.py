def icecream_type(A, B):
    if A + B >= 15 and B >= 8:
        return 1
    elif A + B >= 10 and B >= 3:
        return 2
    elif A + B >= 3:
        return 3
    else:
        return 4

if __name__ == '__main__':
    icecream_type()