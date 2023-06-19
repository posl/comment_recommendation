def is_wonderful_string(s):
    s = list(s)
    s.sort()
    if s[0].islower() and s[-1].isupper():
        return True
    else:
        return False
s = input()
