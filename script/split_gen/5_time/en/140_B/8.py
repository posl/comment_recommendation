def solve(N, A, B, C):
    satisfaction = 0
    for i in range(0, N):
        satisfaction += B[A[i]-1]
        if i < N-1 and A[i+1] == A[i] + 1:
            satisfaction += C[A[i]-1]
    return satisfaction
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
print(solve(N, A, B, C))
