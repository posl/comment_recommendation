def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    res1 = 0
    res2 = 0
    for i in range(N):
        if A[i] == B[i]:
            res1 += 1
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                res2 += 1
    print(res1)
    print(res2)
    
solve()
