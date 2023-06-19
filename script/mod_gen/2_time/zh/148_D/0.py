def solve(N, A):
    if N == 1:
        if A[0] == 1:
            return 0
        else:
            return -1
    else:
        if A[0] != 1:
            return -1
        else:
            for i in range(1, N):
                if A[i] - A[i-1] > 1:
                    return -1
            return N - 1

if __name__ == '__main__':
    solve()