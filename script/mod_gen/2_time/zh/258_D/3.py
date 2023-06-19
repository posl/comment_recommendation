def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for a, b in AB:
        ans += a
        if ans > X:
            print(-1)
            return
        ans += b
    print(ans)

if __name__ == '__main__':
    solve()