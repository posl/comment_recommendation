def solve():
    #input
    N,M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #calculate
    #Aの値が小さい順に並べる
    A,B = zip(*sorted(zip(A,B)))
    #print(A,B)
    ans = 0
    for i in range(N):
        if B[i] >= M:
            ans += A[i] * M
            break
        else:
            ans += A[i] * B[i]
            M -= B[i]
    #output
    print(ans)
