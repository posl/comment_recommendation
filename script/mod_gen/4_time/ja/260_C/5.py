def getStoneNum(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x + y
    return getStoneNum(n-1, x, y) + getStoneNum(n-2, x, y)
n, x, y = map(int, input().split())
print(getStoneNum(n, x, y))

if __name__ == '__main__':
    getStoneNum()