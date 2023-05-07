def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A = sum(A, [])
    A.sort()
    ok = 10**9
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        c = 0
        for i in range(N):
            for j in range(N):
                if A[i * N + j] <= A[mid]:
                    c += 1
        if c >= K * K - (K - 1) * (K - 1):
            ok = mid
        else:
            ng = mid
    print(A[ok])
