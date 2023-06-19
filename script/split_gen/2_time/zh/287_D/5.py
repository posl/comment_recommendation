def match(s, t):
    for i in range(len(s)):
        if s[i] != '?' and t[i] != s[i]:
            return False
    return True
s = input()
t = input()
for i in range(len(s) - len(t) + 1):
    if match(s[i:i+len(t)], t):
        print('Yes')
    else:
        print('No')
