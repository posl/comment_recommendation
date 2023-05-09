def check(s,t):
    if len(t) > len(s):
        return False
    for i in range(len(s)):
        if s[i] == t[0]:
            if s[i:i+len(t)] == t:
                return True
    return False
s = input()
t = input()
