def solve(n, p, q):
    def permutation(n):
        if n == 0:
            return [[]]
        else:
            return [[i] + perm for i in range(1, n + 1) for perm in permutation(n - 1) if i not in perm]
    def index(p):
        return permutation(len(p)).index(p) + 1
    return abs(index(p) - index(q))

if __name__ == '__main__':
    solve()