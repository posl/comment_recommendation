def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        s = 0
        for j in range(i, N):
            s += A[j]
            if s >= K:
                ans += N - j
                break
    print(ans)
