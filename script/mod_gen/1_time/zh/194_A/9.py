def icecream(a,b):
    if a+b >= 15 and b >= 8:
        return 1
    if a+b >= 10 and b >= 3:
        return 2
    if a+b < 10 and b >= 3:
        return 3
    return 4

if __name__ == '__main__':
    icecream()