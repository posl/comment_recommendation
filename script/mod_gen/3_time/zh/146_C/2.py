def d(N):
    if N < 10:
        return 1
    else:
        return 1 + d(N // 10)

if __name__ == '__main__':
    d()