def check(s):
    if len(s) < 3:
        return False
    if s.islower() or s.isupper():
        return False
    if len(s) % 2 != 0:
        return False
    for i in range(0, len(s), 2):
        if s[i] != s[i+1]:
            return False
    return True
s = input()
print("Yes" if check(s) else "No")
