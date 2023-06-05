def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: x[0])
    ans = []
    l = lr[0][0]
    r = lr[0][1]
    for i in range(1, n):
        if lr[i][0] <= r:
            r = max(r, lr[i][1])
        else:
            ans.append([l, r])
            l = lr[i][0]
            r = lr[i][1]
    ans.append([l, r])
    for a in ans:
        print(*a)

if __name__ == '__main__':
    main()