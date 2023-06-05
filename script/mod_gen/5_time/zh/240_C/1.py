def check(X, N, a, b):
    if X == 0:
        return True
    elif N == 0:
        return False
    else:
        return check(X - a[N-1], N-1, a, b) or check(X - b[N-1], N-1, a, b)

if __name__ == '__main__':
    check()