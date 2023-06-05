def solve(x, y, r):
    x1 = int(x * 10000 - r * 10000)
    x2 = int(x * 10000 + r * 10000)
    y1 = int(y * 10000 - r * 10000)
    y2 = int(y * 10000 + r * 10000)
    ans = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if (i - x * 10000) ** 2 + (j - y * 10000) ** 2 <= r * 10000 ** 2:
                ans += 1
    return ans

if __name__ == '__main__':
    solve()