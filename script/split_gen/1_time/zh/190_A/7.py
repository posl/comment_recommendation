def solve(A, B, C):
    if C == 0:
        if A > B:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if B > A:
            return 'Aoki'
        else:
            return 'Takahashi'
