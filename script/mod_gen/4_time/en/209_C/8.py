def solve(N, C):
    A = []
    for i in range(N):
        A.append(C[i] - i - 1)
    A.sort()
    #print(A)
    ans = 1
    for i in range(N):
        if A[i] <= 0:
            return 0
        ans = ans * A[i] % (10**9 + 7)
    return ans

if __name__ == '__main__':
    solve()