def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < N:
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum >= K:
                ans += N - j
                break
        i += 1
    print(ans)

if __name__ == '__main__':
    solve()