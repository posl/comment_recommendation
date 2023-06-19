def get_median(arr):
    arr.sort()
    return arr[(len(arr)-1)//2]
n,k = list(map(int,input().split()))
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
ans = 10**9
for i in range(n-k+1):
    for j in range(n-k+1):
        arr = []
        for x in range(k):
            for y in range(k):
                arr.append(a[i+x][j+y])
        ans = min(ans,get_median(arr))
print(ans)
