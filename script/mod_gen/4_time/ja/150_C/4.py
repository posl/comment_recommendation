def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # 順列生成
    def permutations_count(n, r):
        return math.factorial(n) // math.factorial(n - r)
    def permutations_with_replacement_count(n, r):
        return (n + r - 1) * math.factorial(n - 1) // math.factorial(n - r)
    # 順列生成
    def permutations(iterable, r=None):
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n - r, -1))
        yield tuple(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return
    # 順列生成
    def permutations_with_replacement(iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        for indices in product(range(n), repeat=r):
            if sorted(indices) == list(indices):
                yield tuple(pool[i] for i in indices)
    import math
    from itertools import product
    P_permutations = list(permutations(range(1,N+1)))
    Q_permutations = list(permutations(range(1,N+1)))
    for i in range(len(P_permutations)):
        if P_permutations[i] == tuple(P):
            a = i+1
        if Q_permutations[i] == tuple(Q):
            b = i+1
    print(abs(a-b))
main()

if __name__ == '__main__':
    main()