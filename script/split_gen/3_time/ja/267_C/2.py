def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (i+1) * A[i] - (N-i) * A[i]
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += B[i]
    print(ans)
