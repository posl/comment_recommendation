def median(a):
    a.sort()
    return a[len(a)//2]
n,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
ans=float('inf')
for i in range(n-k+1):
    for j in range(n-k+1):
        temp=[]
        for l in range(k):
            for m in range(k):
                temp.append(a[i+l][j+m])
        ans=min(ans,median(temp))
print(ans)

if __name__ == '__main__':
    median()