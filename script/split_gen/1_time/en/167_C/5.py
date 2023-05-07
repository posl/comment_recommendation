def main():
    # input
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    
    # compute
    ans = -1
    for i in range(2 ** n):
        understanding = [0] * m
        cost = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                cost += c[j]
                understanding = [understanding[k] + a[j][k] for k in range(m)]
        if min(understanding) >= x:
            if ans == -1:
                ans = cost
            else:
                ans = min(ans, cost)
    
    # output
    print(ans)
