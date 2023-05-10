def solve():
    n = int(input())
    trampolines = []
    for i in range(n):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    ans = 1e9
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            xi, yi, pi = trampolines[i]
            xj, yj, pj = trampolines[j]
            d = abs(xi - xj) + abs(yi - yj)
            ans = min(ans, (d + pi - 1) // pi)
    print(ans)
solve()

if __name__ == '__main__':
    solve()