def check(s, t):
    for i in range(len(s)-1):
        if s[i] == t[i]:
            continue
        else:
            if s[i] == t[i+1] and s[i+1] == t[i]:
                return True
            else:
                return False
    return True
s = input()
t = input()
