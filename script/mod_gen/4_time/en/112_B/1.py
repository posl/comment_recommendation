def solve():
    N, T = map(int, input().split())
    ans = T
    for _ in range(N):
        c, t = map(int, input().split())
        if t <= T:
            ans = min(ans, c)
    if ans == T:
        print('TLE')
    else:
        print(ans)

if __name__ == '__main__':
    solve()