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
            xi, yi = map(int, input().split())
            x[i].append(xi)
            y[i].append(yi)
    ans = 0
    for bits in range(1 << n):
        flag = True
        for i in range(n):
            if bits & (1 << i):
                for j in range(a[i]):
                    if ((bits >> (x[i][j] - 1)) & 1) ^ y[i][j]:
                        flag = False
        if flag:
            ans = max(ans, bin(bits).count('1'))
    print(ans)
