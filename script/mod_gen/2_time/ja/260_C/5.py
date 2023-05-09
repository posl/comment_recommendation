def calc(N, X, Y):
    if N == 1:
        return 0
    if N == 2:
        return X + Y
    return calc(N-1, X, Y) + calc(N-2, X, Y)

if __name__ == '__main__':
    calc()