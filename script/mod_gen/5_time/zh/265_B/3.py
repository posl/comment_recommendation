def solve():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(m):
        b.append(list(map(int,input().split())))
    b = sorted(b)
    #print(b)
    i = 0
    for j in range(m):
        if b[j][0] == 1:
            i = j
            break
    #print(i)
    for k in range(i,m):
        if b[k][0] == 1:
            t += b[k][1]
        else:
            break
    #print(t)
    if t < b[i][1]:
        print("No")
        return
    else:
        for i in range(i+1,m):
            t += b[i][1]
        #print(t)
        for i in range(n-1):
            t -= a[i]
            if t <= 0:
                print("No")
                return
        print("Yes")
        return
solve()
