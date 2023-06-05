def findNum(k):
    base = 10
    num = 0
    while k > 0:
        num += base ** (k % 2)
        k = k // 2
    return num

if __name__ == '__main__':
    findNum()