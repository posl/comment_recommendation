def problems226_b():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    ans = []
    for i in range(n):
        if l[i] not in ans:
            ans.append(l[i])
    print(len(ans))
