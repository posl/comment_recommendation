def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        if i == 0:
            ans += A[i]
        else:
            ans += A[i] * (N // A[i] - N // A[i-1])
    print(ans)
