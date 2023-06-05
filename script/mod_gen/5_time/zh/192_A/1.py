def coin(X):
    if X%100 == 0:
        return 100
    else:
        return 100 - X%100

if __name__ == '__main__':
    coin()