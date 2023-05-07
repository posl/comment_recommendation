def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    d = sorted(d.items(), key=lambda x: x[0], reverse=True)
    #print(d)
    num = 0
    for i in range(len(d)):
        num += d[i][1]
        d[i] = (d[i][0], num)
    #print(d)
    ans = []
    for i in range(n):
        l = -1
        r = len(d)
        while r - l > 1:
            c = (l + r) // 2
            if d[c][0] > a[i]:
                l = c
            else:
                r = c
        #print(r)
        if r == len(d):
            ans.append(0)
        else:
            ans.append(d[r][1] - i - 1)
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()