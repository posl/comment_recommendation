def swap_string(s,t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                return True
        return False
