def solve():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(N):
        ans += a[i] * b[i]
    if ans >= X:
        print("Yes")
    else:
        print("No")
