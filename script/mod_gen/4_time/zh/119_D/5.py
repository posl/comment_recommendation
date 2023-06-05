def solve():
    A,B,Q = map(int,input().split())
    s = [0]*A
    t = [0]*B
    x = [0]*Q
    for i in range(A):
        s[i] = int(input())
    for i in range(B):
        t[i] = int(input())
    for i in range(Q):
        x[i] = int(input())
    for i in range(Q):
        ans = 10000000000000000000
        for j in range(A):
            for k in range(B):
                temp = max(s[j],t[k])-min(s[j],t[k])
                temp += min(max(s[j],x[i]),max(x[i],t[k]))-min(max(s[j],x[i]),max(x[i],t[k]))
                temp = min(temp,max(max(s[j],x[i]),max(x[i],t[k]))-min(max(s[j],x[i]),max(x[i],t[k])))
                ans = min(ans,temp)
        print(ans)

if __name__ == '__main__':
    solve()