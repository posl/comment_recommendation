def split(a):
    s=str(a)
    res=[]
    for i in range(len(s)-1):
        res.append((int(s[:i+1]),int(s[i+1:])))
    return res
n=int(input())
res=0
for i,j in split(n):
    res=max(res,i*j)
print(res)
