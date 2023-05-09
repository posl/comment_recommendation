def main():
    N, M, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    A = [0] + A
    B = [0] + B
    for i in range(N):
        A[i+1] += A[i]
    for i in range(M):
        B[i+1] += B[i]
    ans = 0
    j = M
    for i in range(N+1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)
