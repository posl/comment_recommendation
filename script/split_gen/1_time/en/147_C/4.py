def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    x = []
    y = []
    for i in range(n):
        x.append([])
        y.append([])
        for j in range(a[i]):
            xx, yy = map(int, input().split())
            x[i].append(xx)
            y[i].append(yy)
    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(n):
            if (i>>j)&1:
                for k in range(a[j]):
                    if ((i>>(x[j][k]-1))&1) != y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i)[2:].count("1"))
    print(ans)
