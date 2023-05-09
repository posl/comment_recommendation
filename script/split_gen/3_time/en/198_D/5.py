def alphametic(S1, S2, S3):
    if len(S1) < len(S3) or len(S2) < len(S3):
        return "UNSOLVABLE"
    if len(S1) > len(S3) and S1[0] == "0" or len(S2) > len(S3) and S2[0] == "0":
        return "UNSOLVABLE"
    N1 = [0] * len(S1)
    N2 = [0] * len(S2)
    N3 = [0] * len(S3)
    for i in range(len(S3)):
        if S1[-1-i] == S2[-1-i] and S1[-1-i] != S3[-1-i]:
            return "UNSOLVABLE"
        if S1[-1-i] != S2[-1-i] and S1[-1-i] == S3[-1-i]:
            N1[-1-i] = 1
            N2[-1-i] = 1
            N3[-1-i] = 1
        if S1[-1-i] != S2[-1-i] and S2[-1-i] == S3[-1-i]:
            N1[-1-i] = 1
            N2[-1-i] = 1
            N3[-1-i] = 1
    for i in range(len(S3)):
        if S1[-1-i] == S2[-1-i] and S1[-1-i] == S3[-1-i]:
            if N1[-1-i] == 1 and N2[-1-i] == 1:
                N3[-1-i] = 1
            elif N1[-1-i] == 1 and N3[-1-i] == 1:
                N2[-1-i] = 1
            elif N2[-1-i] == 1 and N3[-1-i] == 1:
                N1[-1-i] = 1
            else:
                N1[-1-i] = 1
                N2[-1-i] = 1
                N3[-1-i] = 1
    if N1[0] == 0 and N2[0] == 0 and N3[0] == 0:
        return
