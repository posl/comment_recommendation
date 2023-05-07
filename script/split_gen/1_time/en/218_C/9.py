def findStartPos(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j] == "#":
                return (i, j)
