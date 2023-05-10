def solve(N, M, A, B):
    # write code here
    pass
N, M = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
ans = solve(N, M, A, B)
print(ans)
