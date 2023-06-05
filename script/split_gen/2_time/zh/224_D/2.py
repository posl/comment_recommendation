def main():
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1, y1 = a[i]
                x2, y2 = a[j]
                x3, y3 = a[k]
                x1 -= x3
                x2 -= x3
                y1 -= y3
                y2 -= y3
                s = abs(x1 * y2 - x2 * y1)
                if s > 0 and s % 2 == 0:
                    ans += 1
    print(ans)
main()
