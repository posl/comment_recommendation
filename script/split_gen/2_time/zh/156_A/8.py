def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a for a in A if a < 0] + [0] + [a for a in A if a > 0]
    l = len(A)
    def f(x):
        c = 0
        for a in A:
            if a < 0:
                c += l
            elif a == 0:
                c += l - 1
            else:
                break
            if c >= K:
                return True
        for i in range(l):
            for j in range(i + 1, l):
                if A[i] * A[j] <= x:
                    c += 1
                else:
                    break
                if c >= K:
                    return True
        return False
    ok = 10**18 + 1
    ng = -10**18 - 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(solve())
