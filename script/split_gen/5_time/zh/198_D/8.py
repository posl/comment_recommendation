def solve(s1, s2, s3):
    if len(s1) > len(s3) or len(s2) > len(s3):
        return False
    if len(s1) + len(s2) < len(s3):
        return False
    if len(s1) == 1 and s1 == s3:
        return True
    if len(s2) == 1 and s2 == s3:
        return True
    if len(s3) == 1 and s3 == s1:
        return True
    if len(s3) == 1 and s3 == s2:
        return True
    if len(s1) == 1 and len(s2) == 1:
        if s1 == s3[0] and s2 == s3[1]:
            return True
        if s2 == s3[0] and s1 == s3[1]:
            return True
    if len(s1) == 1:
        for i in range(len(s3)):
            if s1 == s3[i]:
                if solve(s1, s2, s3[:i]) and solve(s1, s2, s3[i+1:]):
                    return True
        return False
    if len(s2) == 1:
        for i in range(len(s3)):
            if s2 == s3[i]:
                if solve(s1, s2, s3[:i]) and solve(s1, s2, s3[i+1:]):
                    return True
        return False
    if len(s1) == 2:
        for i in range(len(s3)):
            if s1[0] == s3[i]:
                for j in range(len(s3)):
                    if s1[1] == s3[j]:
                        if i < j:
                            if solve(s1, s2, s3[:i]) and solve(s1, s2, s3[i+1:j]) and solve(s1, s2, s3[j+1:]):
                                return True
                        else:
                            if solve(s1, s2, s3[:j]) and solve(s1, s2, s3[j+1:i]) and solve(s1, s2, s3[i+1:]):
                                return True
        return False
    if len(s2) == 2:
