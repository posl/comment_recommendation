def solve():
    n,k,q=map(int,input().split())
    a=[0]*n
    for i in range(q):
        a[int(input())-1]+=1
    for i in range(n):
        if q-a[i]>=k:
            print('No')
        else:
            print('Yes')
solve()
