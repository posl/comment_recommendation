def check(s, t):
    for i in range(len(s)):
        if s[i] != '?' and t[i] != '?' and s[i] != t[i]:
            return False
    return True
s = input()
t = input()
for i in range(len(t)+1):
    s1 = s[:i] + t[i:]
    if check(s1, t):
        print('Yes')
    else:
        print('No')
