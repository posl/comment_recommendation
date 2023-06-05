def solve(A,B,K):
    if A == 0:
        return 'b'*B
    if B == 0:
        return 'a'*A
    if K <= 0:
        return 'a'*A + 'b'*B
    if A == 1 and B == 1:
        if K == 1:
            return 'ab'
        else:
            return 'ba'
    if A == 1:
        if K == 1:
            return 'ab' + 'b'*B
        elif K == 2:
            return 'ba' + 'b'*B
        else:
            return 'b'*B + 'a'
    if B == 1:
        if K == 1:
            return 'a'*A + 'ba'
        elif K == 2:
            return 'a'*A + 'ab'
        else:
            return 'b' + 'a'*A
    if K <= 2**(A+B-1):
        return 'a' + solve(A-1,B,K-1)
    else:
        return 'b' + solve(A,B-1,K-2**(A+B-1))

if __name__ == '__main__':
    solve()