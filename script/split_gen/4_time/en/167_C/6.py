def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    cost = 0
    for i in range(2**n):
        bit = []
        for j in range(n):
            if ((i >> j) & 1):
                bit.append(1)
            else:
                bit.append(0)
        if sum(bit)==0:
            continue
        sum_a = [0 for i in range(m)]
        for j in range(n):
            if bit[j]==1:
                for k in range(m):
                    sum_a[k] += a[j][k]
        if min(sum_a)>=x:
            cost = min([cost,sum([c[j]*bit[j] for j in range(n)])])
    if cost==0:
        print(-1)
    else:
        print(cost)
