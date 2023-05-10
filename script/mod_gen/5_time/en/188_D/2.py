def main():
    n, c = map(int, input().split())
    l = []
    for i in range(n):
        a, b, c = map(int, input().split())
        l.append([a, c])
        l.append([b + 1, -c])
    l.sort()
    ans = 0
    fee = 0
    t = 0
    for i in range(2 * n):
        if l[i][0] != t:
            ans += min(c, fee) * (l[i][0] - t)
            t = l[i][0]
        fee += l[i][1]
    print(ans)

if __name__ == '__main__':
    main()