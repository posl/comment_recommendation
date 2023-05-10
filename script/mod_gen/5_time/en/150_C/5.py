def permutations(n):
    if n == 1:
        yield [1]
    else:
        for p in permutations(n - 1):
            for i in range(n):
                yield p[:i] + [n] + p[i:]

if __name__ == '__main__':
    permutations()