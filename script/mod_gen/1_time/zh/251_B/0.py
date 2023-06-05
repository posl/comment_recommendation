def solve(N, W, A):
    A.sort()
    if A[0] > W:
        return 0
    if A[0] + A[1] > W:
        return 1
    if A[0] + A[1] + A[2] > W:
        return 2
    return 3

if __name__ == '__main__':
    solve()