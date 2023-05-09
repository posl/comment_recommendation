def main():
    X, Y = map(float, input().split('.'))
    if Y <= 2:
        print(int(X), '-', sep='')
    elif 3 <= Y <= 6:
        print(int(X))
    elif Y >= 7:
        print(int(X), '+', sep='')
