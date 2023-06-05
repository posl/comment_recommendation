def getNum():
    a,b,c = map(int, input().split())
    if b >= a*c:
        return c
    else:
        return b//a

if __name__ == '__main__':
    getNum()