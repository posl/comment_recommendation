def getMinString(s):
    sLen = len(s)
    minStr = s
    for i in range(1, sLen):
        tmpStr = s[i:] + s[:i]
        if tmpStr < minStr:
            minStr = tmpStr
    return minStr
