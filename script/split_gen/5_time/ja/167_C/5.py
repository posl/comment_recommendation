def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for _ in range(n):
        c_i, *a_i = map(int, input().split())
        c.append(c_i)
        a.append(a_i)
    ans = float('inf')
    for i in range(2**n):
        tmp = [0]*m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                for k in range(m):
                    tmp[k] += a[j][k]
                cost += c[j]
        if all([tmp_i >= x for tmp_i in tmp]):
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
