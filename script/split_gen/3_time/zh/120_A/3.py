def buy_drink(A, B, C):
    if A > B:
        return 0
    else:
        return min(B // A, C)
