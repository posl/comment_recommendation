def main():
    n=int(input())
    a,b=[],[]
    for i in range(n):
        ai,bi=map(int,input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    ans=[0]*n
    for i in range(n):
        ans[0]+=1
        if i!=n-1:
            ans[i+1]-=1
    for i in range(n-1):
        ans[i+1]+=ans[i]
    for i in range(n):
        print(ans[i],end=' ')
    print()
main()
