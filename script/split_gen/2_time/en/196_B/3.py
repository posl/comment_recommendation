def main():
    X = input()
    if X.find('.') != -1:
        X = X[:X.find('.')]
    print(X)
