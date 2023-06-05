def solve():
    n=int(input())
    s=[input() for i in range(n)]
    dic={}
    for i in range(n):
        s[i]="".join(sorted(s[i]))
        if s[i] in dic:
            dic[s[i]]+=1
        else:
            dic[s[i]]=1
    ans=0
    for key in dic:
        ans+=dic[key]*(dic[key]-1)//2
    print(ans)
solve()
