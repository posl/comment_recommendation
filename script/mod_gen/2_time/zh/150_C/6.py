def permutation(n):
    if n == 1:
        return [[1]]
    else:
        return [[n] + p for p in permutation(n-1)] + [p + [n] for p in permutation(n-1)]

if __name__ == '__main__':
    permutation()