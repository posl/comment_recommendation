def check(s, t, x):
    for i in range(x):
        if s[i] != t[i]:
            return False
    for i in range(len(t) - x):
        if s[-1 - i] != t[-1 - i]:
            return False
    return True
s = input()
t = input()
for i in range(len(t) + 1):
    if check(s, t, i):
        print("Yes")
    else:
        print("No")
