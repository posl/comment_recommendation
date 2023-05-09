def main():
    X = input().rstrip()
    if '.' not in X:
        print(X)
    else:
        print(X[0:X.index('.')])
