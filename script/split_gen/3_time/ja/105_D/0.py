def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = (B[i] + A[i]) % M
    D = {}
    for i in range(N + 1):
        if B[i] in D:
            D[B[i]] += 1
        else:
            D[B[i]] = 1
    ans = 0
    for i in D:
        if D[i] > 1:
            ans += D[i] * (D[i] - 1) // 2
    print(ans)
