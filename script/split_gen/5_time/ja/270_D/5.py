def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        if A[i] <= N:
            ans += N % A[i]
            N -= N % A[i]
    print(ans)
