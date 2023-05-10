def solve():
    A, B, X = map(int, input().split())
    def price(n):
        return A * n + B * len(str(n))
    def bisect(ok, ng, p):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if p(mid) <= X:
                ok = mid
            else:
                ng = mid
        return ok
    print(bisect(0, 10 ** 9 + 1, price))
solve()

if __name__ == '__main__':
    solve()