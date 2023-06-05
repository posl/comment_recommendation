def solve(A, B, K):
    if A == 0:
        return 'b' * B
    elif B == 0:
        return 'a' * A
    elif K == 1:
        return 'a' * A + 'b' * B
    elif K == 2 ** (A + B):
        return 'b' * B + 'a' * A
    elif K <= 2 ** (A + B - 1):
        return 'a' + solve(A - 1, B, K - 1)
    else:
        return 'b' + solve(A, B - 1, K - 2 ** (A + B - 1))

if __name__ == '__main__':
    solve()