def get_coins(A, B):
    if A >= B:
        return A + (A-1)
    else:
        return B + (B-1)

if __name__ == '__main__':
    get_coins()