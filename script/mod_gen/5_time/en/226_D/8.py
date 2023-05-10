def main():
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    l = sorted(l, key=lambda x: (x[0], x[1]))
    d = {}
    for i in range(n):
        for j in range(i+1, n):
            dx = l[j][0] - l[i][0]
            dy = l[j][1] - l[i][1]
            if (dx, dy) in d:
                d[(dx, dy)] += 1
            else:
                d[(dx, dy)] = 1
    mx = 0
    for v in d.values():
        mx = max(mx, v)
    print(n-mx)

if __name__ == '__main__':
    main()