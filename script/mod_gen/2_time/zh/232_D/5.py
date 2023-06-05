def check(perm, a, b):
    for i in range(len(a)):
        if perm[a[i]-1] > perm[b[i]-1]:
            return False
    return True
n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
c = []
d = []
for i in range(m):
    x, y = map(int, input().split())
    c.append(x)
    d.append(y)
p = [i for i in range(1, n+1)]
ans = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        p[i-1], p[j-1] = p[j-1], p[i-1]
        if check(p, a, b) and check(p, c, d):
            ans += 1
        p[i-1], p[j-1] = p[j-1], p[i-1]

if __name__ == '__main__':
    check()