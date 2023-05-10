def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(B)
    #print(C)
    cnt = 0
    for i in range(N):
        cnt += B[C[i]-1] == A[i]
    print(cnt)
