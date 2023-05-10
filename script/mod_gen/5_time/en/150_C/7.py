def permutation(n):
    if n == 0:
        return [[]]
    else:
        return [[x] + y for x in range(n) for y in permutation(n - 1) if x not in y]

if __name__ == '__main__':
    permutation()