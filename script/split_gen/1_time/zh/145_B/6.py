def find_substring(s):
    s_len = len(s)
    for i in range(1, s_len//2+1):
        if s_len%i != 0:
            continue
        else:
            if s[:i]*(s_len//i) == s:
                return True
    return False
