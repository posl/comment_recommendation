def main():
    n, c = map(int, input().split())
    l = []
    for i in range(n):
        a, b, d = map(int, input().split())
        l.append([a, d])
        l.append([b+1, -d])
    l.sort()
    s = 0
    ans = 0
    t = 0
    for i in range(len(l)):
        if l[i][0] != t:
            ans += min(c, s) * (l[i][0] - t)
            t = l[i][0]
        s += l[i][1]
    print(ans)

if __name__ == '__main__':
    main()