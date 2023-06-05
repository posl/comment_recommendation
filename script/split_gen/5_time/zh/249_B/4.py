def isWonderfulString(s):
    if len(s) < 2:
        return False
    #判断是否包含大写字母
    hasUpper = False
    for i in range(len(s)):
        if s[i].isupper():
            hasUpper = True
            break
    if not hasUpper:
        return False
    #判断是否包含小写字母
    hasLower = False
    for i in range(len(s)):
        if s[i].islower():
            hasLower = True
            break
    if not hasLower:
        return False
    #判断是否所有的字符都是成对的
    for i in range(len(s)):
        if s.count(s[i]) % 2 != 0:
            return False
    return True
