def main():
    n, d = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[0])
    ans = 0
    r = 0
    for i in range(n):
        if l[i][1] <= r:
            continue
        if l[i][0] > r:
            r = l[i][0]
        ans += (l[i][1] - r) // d + 1
        r += ((l[i][1] - r) // d + 1) * d
    print(ans)

if __name__ == '__main__':
    main()