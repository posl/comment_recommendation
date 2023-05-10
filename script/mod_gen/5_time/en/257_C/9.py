def countAdults(children, adults, X):
    if children >= X:
        return adults
    else:
        return adults + children - X

if __name__ == '__main__':
    countAdults()