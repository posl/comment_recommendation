def getInteger(D, N):
    if D == 0:
        return N
    elif D == 1:
        return N * 100
    elif D == 2:
        return N * 10000
D, N = map(int, input().split())
print(getInteger(D, N))

if __name__ == '__main__':
    getInteger()