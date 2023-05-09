def judge(a,b,s):
    return (4*a*b+3*a+3*b)==s
n=int(input())
s=list(map(int,input().split()))
ans=0
for i in range(n):
    for j in range(1,1001):
        if(judge(j,s[i])):
            ans+=1
            break
print(n-ans)

if __name__ == '__main__':
    judge()