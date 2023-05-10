def calc(N, X, Y):
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return X + Y
    else:
        return calc(N-1, X, Y) + calc(N-2, X, Y)
N, X, Y = map(int, input().split())
print(calc(N, X, Y))

if __name__ == '__main__':
    calc()