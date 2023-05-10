def makeS(n):
    if n == 1:
        return [1]
    else:
        return makeS(n-1) + [n] + makeS(n-1)
N = int(input())
print(*makeS(N))

if __name__ == '__main__':
    makeS()