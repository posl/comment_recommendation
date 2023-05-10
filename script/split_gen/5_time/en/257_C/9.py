def countAdults(children, adults, X):
    if children >= X:
        return adults
    else:
        return adults + children - X
