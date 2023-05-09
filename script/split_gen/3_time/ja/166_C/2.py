def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0 for i in range(M)]
    B = [0 for i in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    good = [True for i in range(N)]
    for i in range(M):
        if H[A[i]] >= H[B[i]]:
            good[B[i]] = False
        if H[B[i]] >= H[A[i]]:
            good[A[i]] = False
    ans = 0
    for i in range(N):
        if good[i]:
            ans += 1
    print(ans)
