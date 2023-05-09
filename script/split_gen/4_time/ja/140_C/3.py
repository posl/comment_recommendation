def solve():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[1] = B[0]
    for i in range(1, N-1):
        A[i+1] = min(B[i-1], B[i])
    print(sum(A))
