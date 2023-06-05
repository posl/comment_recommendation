def get_intersection(l1, r1, l2, r2):
    if r1 < l2 or r2 < l1:
        return 0
    else:
        return min(r1, r2) - max(l1, l2) + 1
n = int(input())
t = []
l = []
r = []
for i in range(n):
    t_i, l_i, r_i = map(int, input().split())
    t.append(t_i)
    l.append(l_i)
    r.append(r_i)
res = 0
for i in range(n):
    for j in range(i+1, n):
        if t[i] == 1 or t[i] == 3:
            if t[j] == 1 or t[j] == 2:
                res += get_intersection(l[i], r[i], l[j], r[j])
        elif t[i] == 2 or t[i] == 4:
            if t[j] == 3 or t[j] == 4:
                res += get_intersection(l[i], r[i], l[j], r[j])
print(res)

if __name__ == '__main__':
    get_intersection()