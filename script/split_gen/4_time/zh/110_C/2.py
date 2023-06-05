def solve(s, t):
    if len(s) != len(t):
        return False
    
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1
        if t[i] not in t_dict:
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] += 1
    
    for k, v in s_dict.items():
        if k not in t_dict:
            return False
        if t_dict[k] != v:
            return False
    
    return True
