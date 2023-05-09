def main():
    X = input()
    if '.' in X:
        print(X[:X.find('.')])
    else:
        print(X)
