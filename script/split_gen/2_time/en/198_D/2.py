def solve(S1,S2,S3):
    if len(S1) < len(S2):
        S1,S2 = S2,S1
    if len(S1) < len(S3):
        S1,S3 = S3,S1
    if len(S2) < len(S3):
        S2,S3 = S3,S2
    if len(S1) > 10 or len(S2) > 10 or len(S3) > 10:
        return "UNSOLVABLE"
    if len(S1) == len(S2) and len(S1) == len(S3):
        if S1 == S2 and S1 == S3:
            return "UNSOLVABLE"
        else:
            for i in range(1,len(S1)):
                if S1[i] != S2[i] or S1[i] != S3[i] or S2[i] != S3[i]:
                    return "UNSOLVABLE"
            return "1
1
2"
    elif len(S1) == len(S2) and len(S1) > len(S3):
        if S1 == S2:
            return "UNSOLVABLE"
        else:
            for i in range(1,len(S1)):
                if S1[i] != S2[i]:
                    return "UNSOLVABLE"
            for i in range(len(S3)):
                if S3[i] == S1[0] or S3[i] == S2[0]:
                    return "UNSOLVABLE"
            return "1
1
2"
    elif len(S1) > len(S2) and len(S1) == len(S3):
        if S1 == S3:
            return "UNSOLVABLE"
        else:
            for i in range(1,len(S1)):
                if S1[i] != S3[i]:
                    return "UNSOLVABLE"
            for i in range(len(S2)):
                if S2[i] == S1[0] or S2[i] == S3[0]:
                    return "UNSOLVABLE"
            return "1
1
2"
    elif len(S1) > len(S2) and len(S1) > len(S3):
        for i in range(len(S3)):
            if S3[i] == S1[0] or S3[i] == S
