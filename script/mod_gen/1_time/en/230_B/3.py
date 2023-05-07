def isSubStr(s, t):
    for i in range(len(t) - len(s) + 1):
        if t[i:i+len(s)] == s:
            return True
    return False
s = input()
t = 'oxx' * 10**5

if __name__ == '__main__':
    isSubStr()