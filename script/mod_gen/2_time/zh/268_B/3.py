def is_prefix(s,t):
    if len(s) > len(t):
        return 'No'
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                return 'No'
        return 'Yes'
s = input()
t = input()
print(is_prefix(s,t))
