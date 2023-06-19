def getKthNum(n, q, a, k):
    a.sort()
    num = 0
    for i in range(1, 10**18):
        if i not in a:
            num += 1
            if num == k:
                return i

if __name__ == '__main__':
    getKthNum()