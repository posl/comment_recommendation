def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
n=int(input())
a=list(map(int,input().split()))
ans=0
ans_n=0
for i in range(2,1001):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans_n:
        ans_n=cnt
        ans=i
print(ans)

if __name__ == '__main__':
    gcd()