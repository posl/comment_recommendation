def f(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
    return -1
s = input()
print(f(s))
