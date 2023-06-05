def solve(A, B, K):
    if A == 0:
        return 'b'*B
    elif B == 0:
        return 'a'*A
    else:
        if K <= comb(A+B-1, B-1):
            return 'a' + solve(A-1, B, K)
        else:
            return 'b' + solve(A, B-1, K-comb(A+B-1, B-1))

if __name__ == '__main__':
    solve()