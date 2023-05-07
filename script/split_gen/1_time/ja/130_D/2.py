def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum >= K:
                ans += N - j
                break
    print(ans)
