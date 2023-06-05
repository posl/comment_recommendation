def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    d = sorted(d.items(), key=lambda x: x[0])
    #print(d)
    ans = 0
    for i in range(len(d)):
        ans += d[i][1]
        d[i] = (d[i][0], ans)
    #print(d)
    for i in range(n):
        for j in range(len(d)):
            if a[i] == d[j][0]:
                print(d[j][1] - 1)
                break
