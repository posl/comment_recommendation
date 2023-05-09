def main():
    import sys
    from decimal import Decimal
    input = sys.stdin.readline
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    def check(t):
        X = []
        for i in range(N):
            X.append(Decimal(A[i]) - Decimal(B[i]) * Decimal(t))
        X.sort(reverse=True)
        return sum(X[:5]) >= 0
    def binary_search(ok, ng):
        while abs(ok - ng) > 0.000000000000001:
            mid = (ok + ng) / 2
            if check(mid):
                ok = mid
            else:
                ng = mid
        return ok
