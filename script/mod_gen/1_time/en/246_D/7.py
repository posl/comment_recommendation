def search(N):
    a = 0
    b = 0
    while True:
        X = a**3 + a**2*b + a*b**2 + b**3
        if X >= N:
            return X
        if a >= b:
            b += 1
        else:
            a += 1

if __name__ == '__main__':
    search()