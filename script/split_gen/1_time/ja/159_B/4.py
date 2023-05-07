def check(s):
    n = len(s)
    for i in range((n-1)//2):
        if s[i] != s[n-1-i]:
            return False
    return True
s = input()
n = len(s)
