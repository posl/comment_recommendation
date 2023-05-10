def takoyaki():
    N, X, T = map(int, input().split())
    if (N % X) == 0:
        return int(N / X) * T
    else:
        return (int(N / X) + 1) * T
print(takoyaki())

if __name__ == '__main__':
    takoyaki()