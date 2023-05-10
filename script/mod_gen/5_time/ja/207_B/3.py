def solve():
    a, b, c, d = map(int, input().split())
    if b >= c * d:
        print(-1)
        return
    ans = 0
    while a > 0:
        ans += 1
        a -= b
        a += c
    print(ans)

if __name__ == '__main__':
    solve()