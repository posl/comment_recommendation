def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for s in range(1 << n):
        ok = True
        for i in range(n):
            if (s & (1 << i)) == 0:
                continue
            for j in range(i + 1, n):
                if (s & (1 << j)) == 0:
                    continue
                if a[i][j] == 0:
                    ok = False
        if not ok:
            continue
        cur = 0
        for i in range(n):
            if (s & (1 << i)) == 0:
                continue
            for j in range(i + 1, n):
                if (s & (1 << j)) == 0:
                    continue
                cur ^= a[i][j]
        ans = max(ans, cur)
    print(ans)

if __name__ == '__main__':
    main()