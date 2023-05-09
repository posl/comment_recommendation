def check(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
l = len(s)
