def main():
    n = int(input())
    a = [0] * n
    x = [[0] * n for _ in range(n)]
    y = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i] = int(input())
        for j in range(a[i]):
            x[i][j], y[i][j] = map(int, input().split())
            x[i][j] -= 1
    ans = 0
    for i in range(1 << n):
        ok = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if ((i >> x[j][k]) & 1) ^ y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)
