def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        x.append([])
        y.append([])
        for j in range(a[i]):
            x[i].append(0)
            y[i].append(0)
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(2 ** n):
        flag = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if ((i >> (x[j][k] - 1)) & 1) ^ y[j][k]:
                        flag = False
                        break
        if flag:
            ans = max(ans, bin(i).count('1'))
    print(ans)
