def solve(N, A):
    A.sort()
    if A[-1] < 2:
        return -1
    if A[-1] == 2:
        return 2
    for i in range(N-1):
        if A[i] == A[i+1]:
            return A[i]*2
    return -1

if __name__ == '__main__':
    solve()