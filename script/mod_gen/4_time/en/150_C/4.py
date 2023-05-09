def permutations(n):
    if n == 1:
        return [[1]]
    else:
        return [[i] + p for i in range(1, n + 1) for p in permutations(n - 1) if i not in p]

if __name__ == '__main__':
    permutations()