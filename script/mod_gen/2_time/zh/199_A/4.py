def isRight(a,b,c):
    if a**2 + b**2 < c**2:
        return True
    else:
        return False
a,b,c = map(int, input().split())

if __name__ == '__main__':
    isRight()