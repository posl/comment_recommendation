def main():
    a,b,q=map(int,input().split())
    s=[int(input()) for _ in range(a)]
    t=[int(input()) for _ in range(b)]
    x=[int(input()) for _ in range(q)]
    for i in range(q):
        ans=10**11
        for j in range(a):
            for k in range(b):
                if s[j]<=x[i]<=t[k]:
                    ans=min(ans,min(x[i]-s[j],t[k]-x[i])+t[k]-s[j])
                elif x[i]<s[j]:
                    ans=min(ans,s[j]-x[i])
                else:
                    ans=min(ans,x[i]-t[k])
        print(ans)
