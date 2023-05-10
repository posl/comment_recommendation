def solve(N, Q, T, A, B):
    pass
N, Q = map(int, input().split())
T = [0] * Q
A = [0] * Q
B = [0] * Q
for i in range(Q):
    T[i], A[i], B[i] = map(int, input().split())
print(solve(N, Q, T, A, B))
