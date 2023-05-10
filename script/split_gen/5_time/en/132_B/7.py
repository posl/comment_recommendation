def check(s):
    if len(s) != 4:
        return False
    for i in range(0, 4):
        if s.count(s[i]) != 2:
            return False
    return True
s = input()
