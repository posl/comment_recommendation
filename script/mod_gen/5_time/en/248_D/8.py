def solve(N, A, Q, queries):
    ans = []
    for q in queries:
        L, R, X = q
        ans.append(A[L-1:R].count(X))
    return ans

if __name__ == '__main__':
    solve()