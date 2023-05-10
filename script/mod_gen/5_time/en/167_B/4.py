def max_sum(A, B, C, K):
    if K <= A:
        return K
    elif K <= A + B:
        return A
    else:
        return A - (K - A - B)

if __name__ == '__main__':
    max_sum()