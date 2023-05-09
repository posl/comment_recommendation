def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    ans = 0
    for i in range(M, N+1):
        for j in range(N-i+1):
            ans = max(ans, B[i+j]-B[j])
    print(ans)
