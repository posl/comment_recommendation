def main():
    n = int(input())
    lr = []
    for i in range(n):
        l, r = map(int, input().split())
        lr.append([l, r])
    lr.sort()
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
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
main()
