def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    def permutation(n):
        if n == 1:
            yield (0,)
        else:
            for i in range(n):
                for j in permutation(n - 1):
                    yield j + (i,)
    def to_num(p):
        n = len(p)
        num = 0
        for i in range(n):
            num += p[i] * (n ** i)
        return num
    def solve(n, p, q):
        for i, v in enumerate(permutation(n)):
            if p == v:
                p_num = i
            if q == v:
                q_num = i
        return abs(p_num - q_num)
    print(solve(n, p, q))
