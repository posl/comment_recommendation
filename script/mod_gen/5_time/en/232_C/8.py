def solve(N, M, A, B, C, D):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if (i + 1, j + 1) in zip(A, B) and not (i + 1, j + 1) in zip(C, D):
                return False
            if not (i + 1, j + 1) in zip(A, B) and (i + 1, j + 1) in zip(C, D):
                return False
    return True

if __name__ == '__main__':
    solve()