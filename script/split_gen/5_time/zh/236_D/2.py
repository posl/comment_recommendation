def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 2 ** n):
        for j in range(i):
            if i & j == 0:
                s = 0
                for x in range(n):
                    if i & (1 << x):
                        for y in range(x + 1, n):
                            if i & (1 << y):
                                s += a[x][y]
                    if j & (1 << x):
                        for y in range(x + 1, n):
                            if j & (1 << y):
                                s += a[x][y]
                ans = max(ans, s)
    print(ans)
