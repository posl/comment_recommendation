def solve():
    n=int(input())
    s=[input() for _ in range(n)]
    t=[0]*n
    for i in range(n):
        for j in range(10):
            if s[i][j]=='0':
                t[i]=j
                break
    for i in range(n):
        if t[i]==0:
            t[i]=10
    t.sort()
    ans=0
    for i in range(n):
        if i==0:
            ans=t[i]
        elif t[i-1]==t[i]:
            ans+=10
        else:
            ans+=t[i]
    print(ans)

if __name__ == '__main__':
    solve()