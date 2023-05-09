def check(s, t):
    if s == t:
        return True
    if len(s) == len(t):
        return False
    if t[0] == t[1]:
        return check(s, t[1:])
    if t[-1] == t[-2]:
        return check(s, t[:-1])
    return check(s, t[1:-1])
s = input()
t = input()
print("Yes" if check(s, t) else "No")
