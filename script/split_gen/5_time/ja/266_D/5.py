def solve():
    N = int(input())
    A = []
    for i in range(N):
        t,x,a = map(int,input().split())
        A.append((t,x,a))
    A.sort()
    ans = 0
    now = 0
    for a in A:
        t,x,a = a
        if now < x:
            now = x
        if now + a > t:
            ans += a
            now += a
    print(ans)
