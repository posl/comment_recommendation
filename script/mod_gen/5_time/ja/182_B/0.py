def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(2,a[-1]+1):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
print(ans)

if __name__ == '__main__':
    gcd()