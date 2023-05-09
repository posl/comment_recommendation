def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    for x in X:
        ok = N
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if A[mid] >= x:
                ok = mid
            else:
                ng = mid
        print(N - ok)
