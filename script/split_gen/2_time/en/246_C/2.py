def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], K) * (X if A[i] > K else 0)
    print(ans)
