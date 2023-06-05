def check(x,y):
    if y>=0 and y<=2:
        return "X-"
    elif y>=3 and y<=6:
        return "X"
    elif y>=7 and y<=9:
        return "X+"

if __name__ == '__main__':
    check()