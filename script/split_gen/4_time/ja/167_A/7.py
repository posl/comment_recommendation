def is_same(s1, s2):
    if len(s1) != len(s2) - 1:
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True
