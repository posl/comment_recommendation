def get_probability(A, B, C, X):
    if X <= A:
        return 1
    elif X <= B:
        return C / (B - A)
    else:
        return 0

if __name__ == '__main__':
    get_probability()