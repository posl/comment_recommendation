def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    if a[-1]>b[-1]:
        print("No")
        return
    i=0
    for j in range(m):
        if a[i]==b[j]:
            i+=1
            if i==n:
                print("Yes")
                return
    print("No")
solve()
