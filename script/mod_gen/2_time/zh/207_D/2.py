def isMatch(s,t):
    s1 = []
    t1 = []
    for i in range(len(s)):
        s1.append([s[i][0],s[i][1]])
    for i in range(len(t)):
        t1.append([t[i][0],t[i][1]])
    s1.sort()
    t1.sort()
    for i in range(len(s1)):
        if s1[i] != t1[i]:
            return False
    return True

if __name__ == '__main__':
    isMatch()