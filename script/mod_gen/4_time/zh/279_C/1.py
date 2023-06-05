def pattern(s, t):
    s = [list(i) for i in s]
    t = [list(i) for i in t]
    for i in range(len(s)):
        s[i].sort()
        t[i].sort()
        if s[i] != t[i]:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    pattern()