def permutate(n):
    if n == 0:
        return [[]]
    else:
        return [[x] + p for x in range(n) for p in permutate(n - 1) if x not in p]

if __name__ == '__main__':
    permutate()