def f(n, a):
    if n == 0:
        return 0
    if n == 1:
        return a[0][1]
    if n == 2:
        return a[0][1] ^ a[0][2] ^ a[1][2]
    if n == 3:
        return a[0][1] ^ a[0][2] ^ a[0][3] ^ a[1][2] ^ a[1][3] ^ a[2][3]
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                res = max(res, a[i][j] ^ a[i][k] ^ a[j][k] ^ f(n - 3, a))
    return res
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
print(f(n, a))

if __name__ == '__main__':
    f()