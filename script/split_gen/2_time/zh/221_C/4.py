def func(s,t):
    if s==t:
        return True
    else:
        for i in range(len(s)-1):
            if s[i+1]+s[i]==t[i+1]+t[i]:
                return True
    return False
