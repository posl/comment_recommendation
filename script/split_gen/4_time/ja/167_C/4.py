def main():
    n,m,x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = -1
    for i in range(1 << n):
        cost = 0
        skill = [0] * m
        for j in range(n):
            if i >> j & 1:
                cost += c[j]
                for k in range(m):
                    skill[k] += a[j][k]
        if min(skill) >= x:
            if ans == -1:
                ans = cost
            else:
                ans = min(ans, cost)
    print(ans)
