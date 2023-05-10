def intersect(a, b, c, d):
    if a <= c and c < b:
        return True
    if a < d and d <= b:
        return True
    if c <= a and a < d:
        return True
    if c < b and b <= d:
        return True
    return False
n = int(input())
t = []
l = []
r = []
for i in range(n):
    t_i, l_i, r_i = map(int, input().split())
    t.append(t_i)
    l.append(l_i)
    r.append(r_i)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if intersect(l[i], r[i], l[j], r[j]) == True:
            ans += 1
print(ans)

if __name__ == '__main__':
    intersect()