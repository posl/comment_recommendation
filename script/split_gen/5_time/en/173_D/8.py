def solve():
    N = int(input())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(1,N):
        sum += min(A[i-1],A[i])
    print(sum+max(A[0],A[N-1]))
