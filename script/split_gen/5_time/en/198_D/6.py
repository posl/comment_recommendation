def is_valid(S1, S2, S3, N1, N2, N3):
    # print("is_valid", S1, S2, S3, N1, N2, N3)
    if len(S1) != len(N1) or len(S2) != len(N2) or len(S3) != len(N3):
        return False
    if N1[0] == '0' or N2[0] == '0' or N3[0] == '0':
        return False
    for i in range(len(S1)):
        if S1[i] == S2[i] and N1[i] != N2[i]:
            return False
        if S1[i] == S3[i] and N1[i] != N3[i]:
            return False
        if S2[i] == S3[i] and N2[i] != N3[i]:
            return False
    return True
