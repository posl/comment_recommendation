def solve(s,t):
    s = list(s)
    t = list(t)
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            if s[i] in t:
                if t[i] in s:
                    s[i],t[i] = t[i],s[i]
                else:
                    return False
            else:
                return False
    return True
s = input()
t = input()
