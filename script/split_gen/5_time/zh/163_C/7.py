def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(1,N):
        B[A[i-1]-1] += 1
    for i in range(N):
        print(B[i])
