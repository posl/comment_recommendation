def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    ans = 0
    for i in range(N):
        ans = max(ans, A[i + 1] - A[i])
    print(K - ans)
