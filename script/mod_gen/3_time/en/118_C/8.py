def solve(N, A):
    A = sorted(A, reverse=True)
    if N == 2:
        return A[0]
    else:
        return max(1, A[0]-sum(A[1:N-1])+1)

if __name__ == '__main__':
    solve()