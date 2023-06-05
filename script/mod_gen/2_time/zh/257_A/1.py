def main():
    n = int(input())
    a = []
    for _ in range(n):
        l, r = map(int, input().split())
        a.append((l, r))
    a.sort()
    ans = []
    l, r = a[0]
    for i in range(1, n):
        if a[i][0] <= r:
            r = max(r, a[i][1])
        else:
            ans.append((l, r))
            l, r = a[i]
    ans.append((l, r))
    for l, r in ans:
        print(l, r)

if __name__ == '__main__':
    main()