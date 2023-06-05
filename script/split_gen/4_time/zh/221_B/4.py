def is_exchangeable(s,t):
    if s == t:
        return True
    else:
        s = list(s)
        t = list(t)
        for i in range(len(s)-1):
            s[i],s[i+1] = s[i+1],s[i]
            if s == t:
                return True
            else:
                s[i],s[i+1] = s[i+1],s[i]
        return False
s = input()
t = input()
