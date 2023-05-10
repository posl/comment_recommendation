def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort()
    ans = []
    l = lr[0][0]
    r = lr[0][1]
    for i in range(1, n):
        if r < lr[i][0]:
            ans.append([l, r])
            l = lr[i][0]
            r = lr[i][1]
        else:
            r = max(r, lr[i][1])
    ans.append([l, r])
    for a in ans:
        print(a[0], a[1])

if __name__ == '__main__':
    main()