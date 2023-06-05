def func(s,t):
    if len(s) > len(t):
        return "No"
    i = 0
    for j in range(len(t)):
        if i < len(s) and s[i] == t[j]:
            i += 1
    if i == len(s):
        return "Yes"
    else:
        return "No"
s = input()
t = input()
print(func(s,t))
