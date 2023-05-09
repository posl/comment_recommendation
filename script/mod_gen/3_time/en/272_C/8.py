def solve(N, A):
    A.sort()
    if A[-1] % 2 == 1:
        return -1
    else:
        return A[-1]

if __name__ == '__main__':
    solve()