def solve(N, A):
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] - (A[i-1] + A[(i+1)%N]) // 2
    return ans

if __name__ == '__main__':
    solve()