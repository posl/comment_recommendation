def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n // 10)
A, B, X = map(int, input().split())

if __name__ == '__main__':
    d()