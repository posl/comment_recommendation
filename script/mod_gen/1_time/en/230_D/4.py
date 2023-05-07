def main():
    n, d = map(int, input().split())
    l, r = [], []
    for _ in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    l.sort()
    r.sort()
    ans = 0
    for i in range(n):
        ans += l[i] + r[i] - d
    print(ans)

if __name__ == '__main__':
    main()