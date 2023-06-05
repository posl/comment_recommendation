def solve():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    ans = 0
    for i in range(n):
        ans += a[i]*b[i]
    if ans <= x:
        print("Yes")
    else:
        print("No")
