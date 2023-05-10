def solve():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    #print(N,A,X)
    #print(A*N)
    B = A*N
    #print(B)
    ans = 0
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            ans = i+1
            break
    print(ans)
    return 0
