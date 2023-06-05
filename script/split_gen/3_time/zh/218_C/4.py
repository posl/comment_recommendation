def rotate90(s):
    s2 = s[:]
    for i in range(len(s)):
        for j in range(len(s)):
            s2[j][len(s)-i-1] = s[i][j]
    return s2
