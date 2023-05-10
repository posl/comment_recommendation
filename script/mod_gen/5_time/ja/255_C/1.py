def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return -1
    if (x - a) % d != 0:
        return -1
    ans = 0
    if (x - a) // d > 0:
        ans += (x - a) // d
        x -= (x - a) // d * d
    else:
        ans += -((x - a) // d)
        x -= -((x - a) // d) * d
    if x != a:
        ans += 1
        x -= d
    if x != a:
        ans += 1
    return ans
x, a, d, n = map(int, input().split())
print(solve(x, a, d, n))

if __name__ == '__main__':
    solve()