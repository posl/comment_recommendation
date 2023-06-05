def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: x[0])
    ans = 0
    for i in range(len(d)):
        if i == 0:
            ans += d[i][1]
            print(ans)
        else:
            ans += d[i][1]
            if d[i][0] == d[i-1][0]:
                print(ans - d[i][1])
            else:
                print(ans)
