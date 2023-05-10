def solver():
    N = int(input())
    A = sorted(list(map(int,input().split())))
    #print(A)
    ans = 0
    for i in range(1,N):
        ans += A[i] - A[i-1]
        #print(ans)
    ans *= 2
    ans += A[N-1] - A[0]
    print(ans)
    return 0
