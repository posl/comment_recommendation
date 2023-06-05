def rotateString(s, t):
    if s == t:
        return 'Yes'
    else:
        for i in range(len(s)):
            s = s[len(s)-1]+s[:len(s)-1]
            if s == t:
                return 'Yes'
        return 'No'
