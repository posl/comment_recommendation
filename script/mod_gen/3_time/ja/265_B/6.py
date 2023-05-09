def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    now = 0
    for x,y in XY:
        now += A[x-1]
        now = min(now+T-y,T)
    now += A[N-2]
    if now >= T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()