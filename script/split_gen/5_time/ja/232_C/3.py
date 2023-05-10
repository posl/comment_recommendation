def check(a, b, p):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and b[i] != b[j]:
                return False
            if a[i] != a[j] and b[i] == b[j]:
                return False
            if a[i] == a[j] and b[i] == b[j]:
                if p[i] != p[j]:
                    return False
    return True
n, m = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(m):
    tmp_a, tmp_b = map(int, input().split())
    a.append(tmp_a)
    b.append(tmp_b)
for i in range(m):
    tmp_c, tmp_d = map(int, input().split())
    c.append(tmp_c)
    d.append(tmp_d)
p = [i for i in range(1, n+1)]
ans = "No"
for i in range(2**n):
    tmp = []
    for j in range(n):
        if (i >> j) & 1:
            tmp.append(p[j])
    if len(tmp) == n:
        if check(a, b, tmp) and check(c, d, tmp):
            ans = "Yes"
print(ans)
