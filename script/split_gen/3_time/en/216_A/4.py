def main():
    X, Y = input().split('.')
    Y = int(Y)
    if Y <= 2:
        print(X + '-')
    elif Y <= 6:
        print(X)
    else:
        print(X + '+')
