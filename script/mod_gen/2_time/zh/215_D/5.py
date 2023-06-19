def gcd(a,b):
    if a>b:
        a,b=b,a
    if a==0:
        return b
    return gcd(b%a,a)
n,m=map(int,input().split())
a=list(map(int,input().split()))
max_a=max(a)
cnt=[0]*(max_a+1)
for i in range(n):
    cnt[a[i]]+=1
ans=[]
for i in range(1,max_a+1):
    if cnt[i]==0:
        continue
    if gcd(i,max_a)==1:
        ans.append(i)
for i in range(1,m+1):
    if gcd(i,max_a)==1:
        ans.append(i)
ans=set(ans)
ans=list(ans)
ans.sort()
print(len(ans))
for i in ans:
    print(i)

if __name__ == '__main__':
    gcd()