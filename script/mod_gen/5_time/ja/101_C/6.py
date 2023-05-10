def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if (N - K) % (K - 1) == 0:
        ans += (N - K) // (K - 1)
    else:
        ans += (N - K) // (K - 1) + 1
    print(ans + 1)

if __name__ == '__main__':
    solve()