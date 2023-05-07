def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort()
    ans = 0
    for i in range(m):
        a, b = ab[i]
        for j in range(i + 1, m):
            c, d = ab[j]
            if a <= c <= b:
                if b <= d:
                    ans += (b - c) * (b - c + 1) // 2
                else:
                    ans += (d - c) * (d - c + 1) // 2
            elif c <= a <= d:
                if d <= b:
                    ans += (d - a) * (d - a + 1) // 2
                else:
                    ans += (b - a) * (b - a + 1) // 2
    print(ans)
