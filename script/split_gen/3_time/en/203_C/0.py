def main():
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = [0] + A + [10**100]
    B = [0] + B + [0]
    A = sorted(A)
    B = sorted(B)
    ans = 0
    for i in range(N + 1):
        if K >= A[i + 1] - A[i]:
            K -= A[i + 1] - A[i]
            ans = A[i + 1]
        else:
            ans += K
            K = 0
            break
    for i in range(N + 1):
        if K >= B[i + 1] - B[i]:
            K -= B[i + 1] - B[i]
            ans = B[i + 1]
        else:
            ans += K
            K = 0
            break
    print(ans)
