def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    for i in range(N):
        B[A[i]] += 1
    C = [0] * M
    for i in range(M):
        C[(i+1)%M] += B[i]
    ans = 0
    for i in range(M):
        ans += min(B[i], C[i])
    print(ans)
