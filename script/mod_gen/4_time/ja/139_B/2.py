def solve():
    a, b = map(int, input().split())
    ans = 0
    while b > 0:
        ans += 1
        b -= a - 1
    print(ans)

if __name__ == '__main__':
    solve()