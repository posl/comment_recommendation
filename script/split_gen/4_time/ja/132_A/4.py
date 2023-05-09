def check(s):
    l = list(s)
    l.sort()
    if l[0] == l[1] and l[2] == l[3] and l[0] != l[2]:
        return True
    else:
        return False
s = input()
