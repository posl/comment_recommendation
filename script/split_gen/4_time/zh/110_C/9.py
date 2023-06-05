def change(S, T):
    s = list(S)
    t = list(T)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if t[i] == t[j]:
                    continue
                else:
                    return False
            elif s[i] == t[j]:
                if t[i] == s[j]:
                    continue
                else:
                    return False
            elif s[i] == t[i]:
                if s[j] == t[j]:
                    continue
                else:
                    return False
            else:
                continue
    return True
