def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        t.append(tmp[0])
        k.append(tmp[1])
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        if k[i] == 0:
            ans = max(ans, t[i])
        else:
            tmp = 0
            for j in range(k[i]):
                tmp = max(tmp, t[a[i][j]-1])
            ans = max(ans, tmp+t[i])
    print(ans)
