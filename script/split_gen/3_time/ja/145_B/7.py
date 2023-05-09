def isDouble(s):
    if len(s) % 2 != 0:
        return False
    else:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        if s1 == s2:
            return True
        else:
            return False
N = int(input())
S = input()
