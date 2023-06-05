def solve(N, M, T, A, B):
    # 你的代码
    return 'Yes'
N, M, T = map(int, input().split())
A, B = [], []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
print(solve(N, M, T, A, B))
