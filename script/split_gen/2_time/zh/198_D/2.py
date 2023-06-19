def solve(s1,s2,s3):
    #print(s1,s2,s3)
    s1_len = len(s1)
    s2_len = len(s2)
    s3_len = len(s3)
    s1_set = set(s1)
    s2_set = set(s2)
    s3_set = set(s3)
    s_set = s1_set.union(s2_set).union(s3_set)
    #print(s1_set,s2_set,s3_set,s_set)
    if len(s_set) > 10:
        return False
    if s1_len > s3_len or s2_len > s3_len:
        return False
    if s1_len < s3_len and s2_len < s3_len:
        return False
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if i in s_set and j in s_set and k in s_set:
                    if s1_len == s3_len:
                        if s1.count(list(s_set)[i]) != s3.count(list(s_set)[i]):
                            return False
                    if s2_len == s3_len:
                        if s2.count(list(s_set)[j]) != s3.count(list(s_set)[j]):
                            return False
                    if s1_len == s3_len and s2_len == s3_len:
                        if s1.count(list(s_set)[i]) + s2.count(list(s_set)[j]) != s3.count(list(s_set)[k]):
                            return False
                    if s1_len < s3_len:
                        if s3.count(list(s_set)[k]) - s1.count(list(s_set)[i]) != s2.count(list(s_set)[j]):
                            return False
                    if s2_len < s3_len:
                        if s3.count(list(s_set)[k]) - s2.count(list(s_set)[j]) != s1.count(list(s_set)[i]):
                            return False
    return True
