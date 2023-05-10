def solve():
    X,Y,N = map(int,input().split())
    ans = 0
    if N % 3 == 0:
        ans = (N // 3) * Y
    elif N % 3 == 1:
        ans = (N // 3) * Y + X
    else:
        ans = (N // 3) * Y + Y
    print(ans)
