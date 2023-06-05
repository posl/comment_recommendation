def check(s):
    n = len(s)
    for i in range(n//2):
        if s[:i+1] == s[i+1:2*i+2]:
            return True
    return False
n = int(input())
s = input()
