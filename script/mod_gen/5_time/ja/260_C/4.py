def calc(N, X, Y):
    if N == 1:
        return 0
    else:
        return (N-1) * min(X, Y)

if __name__ == '__main__':
    calc()