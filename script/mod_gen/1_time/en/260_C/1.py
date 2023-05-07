def calc(N,X,Y):
    if N == 1:
        return 0
    elif N == 2:
        return X + Y
    else:
        return calc(N-1,X,Y) + X + calc(N-1,X,Y) + Y

if __name__ == '__main__':
    calc()