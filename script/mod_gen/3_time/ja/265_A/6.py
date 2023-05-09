def calc(N, X, Y):
    if N <= 3:
        return X*N
    else:
        return calc(N-3, X, Y) + Y

if __name__ == '__main__':
    calc()