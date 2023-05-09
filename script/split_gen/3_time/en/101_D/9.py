def snuke(k):
    def sum_digits(n):
        return sum([int(x) for x in str(n)])
    def snuke_gen():
        yield 1
        for i in range(2, 10**15):
            if i % sum_digits(i) == 0:
                yield i
    return list(itertools.islice(snuke_gen(), k))
