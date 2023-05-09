def alphametic(S1, S2, S3):
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N2 or N1 < N3:
        return 'UNSOLVABLE'
    if N1 == N2 and N1 == N3:
        if S1 == S2 == S3:
            return 'UNSOLVABLE'
        if S1[0] == S2[0] == S3[0]:
            return 'UNSOLVABLE'
    if N1 == N2 and N1 > N3:
        if S1[0] == S2[0] and S1[0] == S3[0]:
            return 'UNSOLVABLE'
        if S1[0] == S2[0] and S1[0] != S3[0]:
            return 'UNSOLVABLE'
    if N1 == N3 and N1 > N2:
        if S1[0] == S3[0] and S1[0] == S2[0]:
            return 'UNSOLVABLE'
        if S1[0] == S3[0] and S1[0] != S2[0]:
            return 'UNSOLVABLE'
    if N2 == N3 and N2 > N1:
        if S2[0] == S3[0] and S2[0] == S1[0]:
            return 'UNSOLVABLE'
        if S2[0] == S3[0] and S2[0] != S1[0]:
            return 'UNSOLVABLE'
    if N1 > N2 and N1 > N3:
        if S1[0] == S2[0] == S3[0]:
            return 'UNSOLVABLE'
        if S1[0] == S2[0] and S1[0] != S3[0]:
            return 'UNSOLVABLE'
        if S1[0] == S3[0] and S1[0] != S2[0]:
            return 'UNSOLVABLE'
        if S2[0] == S3[0] and S2[0] != S1[0]:
            return 'UNSOLVABLE'
    if

if __name__ == '__main__':
    alphametic()