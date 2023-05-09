def isok(n,x):
    if n==0:
        return True
    if n%2==1:
        return isok(n//2,x//2)
    else:
        return (x%2==0 and isok(n//2,x//2))
n=int(input())
ans=[]
for i in range(0,2**15):
    if isok(n,i):
        ans.append(i)
print(*ans,sep='\n')
