def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    #print(c)
    #print(a)
    min_cost = 1000000000
    for i in range(2**n):
        total_cost = 0
        total_a = [0]*m
        for j in range(n):
            if ((i>>j) & 1):
                total_cost += c[j]
                for k in range(m):
                    total_a[k] += a[j][k]
        flag = True
        for k in range(m):
            if total_a[k] < x:
                flag = False
                break
        if flag:
            min_cost = min(min_cost,total_cost)
    if min_cost == 1000000000:
        print(-1)
    else:
        print(min_cost)
