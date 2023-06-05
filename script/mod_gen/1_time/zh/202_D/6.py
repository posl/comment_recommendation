def solve(A, B, K):
    if A == 0:
        return 'b' * B
    elif B == 0:
        return 'a' * A
    elif K <= comb(A + B - 1, B):
        return 'a' + solve(A - 1, B, K)
    else:
        return 'b' + solve(A, B - 1, K - comb(A + B - 1, B))

if __name__ == '__main__':
    solve()