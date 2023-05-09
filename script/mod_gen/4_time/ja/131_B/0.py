def solve():
    N, L = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        ans += L + i - 1
    if L > 0:
        ans -= L + N - 1
    elif L+N-1 < 0:
        ans -= L
    print(ans)

if __name__ == '__main__':
    solve()