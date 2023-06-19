def solve(S1, S2, S3):
    if len(S1) < len(S3):
        S1, S3 = S3, S1
    if len(S2) < len(S3):
        S2, S3 = S3, S2
    if len(S1) < len(S2):
        S1, S2 = S2, S1
    if len(S1) < len(S3):
        S1, S3 = S3, S1
    if len(S2) < len(S3):
        S2, S3 = S3, S2
    if len(S1) != len(S2) + len(S3):
        return "UNSOLVABLE"
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if len(S1) == len(S2) + len(S3):
                    if S1.count(str(i)) == S2.count(str(j)) + S3.count(str(k)):
                        if S1.count(str(i)) == 1:
                            if S1.index(str(i)) > S2.index(str(j)) + S3.index(str(k)):
                                return "UNSOLVABLE"
                        else:
                            if S1.index(str(i)) < S2.index(str(j)) + S3.index(str(k)):
                                return "UNSOLVABLE"
                    else:
                        return "UNSOLVABLE"
    return "UNSOLVABLE"
S1 = input()
S2 = input()
S3 = input()
print(solve(S1, S2, S3))
