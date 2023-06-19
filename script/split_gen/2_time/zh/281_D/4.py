def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # K = 1
    if K == 1:
        if D % A[0] == 0:
            print(-1)
        else:
            print(A[0])
        return
    # K >= 2
    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            if D % (A[i] + A[j]) == 0:
                continue
            if ans == -1:
                ans = A[i] + A[j]
            else:
                ans = min(ans, A[i] + A[j])
    print(ans)
