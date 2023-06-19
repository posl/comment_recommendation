def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    #print(N,M,T,A,XY)
    ans = 'No'
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            break
        for xy in XY:
            if i+1 == xy[0]:
                time += xy[1]
        if i+1 == N-1 and time > 0:
            ans = 'Yes'
    print(ans)
