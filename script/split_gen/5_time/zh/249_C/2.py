def check(s1,s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            return False
    return True
