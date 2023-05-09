def solve(N, A, B):
    if A == 0:
        return 0
    if B == 0:
        return N
    q, r = divmod(N, A + B)
    return q * A + min(r, A)
N, A, B = map(int, input().split())
print(solve(N, A, B))
