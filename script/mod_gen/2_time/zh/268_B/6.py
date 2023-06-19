def isPrefix(s, t):
    if len(s) > len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True
S = input()
T = input()

if __name__ == '__main__':
    isPrefix()