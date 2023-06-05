def solve(A, B, K):
    if K <= A:
        return A - K, B
    elif K <= A + B:
        return 0, B - (K - A)
    else:
        return 0, 0

if __name__ == '__main__':
    solve()