def d(N):
    if N < 10:
        return 1
    else:
        return d(N//10) + 1

if __name__ == '__main__':
    d()