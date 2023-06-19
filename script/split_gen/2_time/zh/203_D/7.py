def median(lst):
    lst.sort()
    if len(lst)%2==0:
        return (lst[len(lst)//2-1]+lst[len(lst)//2])/2
    else:
        return lst[len(lst)//2]
n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
ans=1000000000
for i in range(n-k+1):
    for j in range(n-k+1):
        lst=[]
        for x in range(k):
            for y in range(k):
                lst.append(a[i+x][j+y])
        ans=min(ans,median(lst))
print(int(ans))
