def solve(A, B):
    if A == B:
        return A
    else:
        return solve(A, B-1) ^ B

if __name__ == '__main__':
    solve()