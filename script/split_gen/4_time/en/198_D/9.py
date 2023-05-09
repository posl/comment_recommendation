def getNum(s, chars):
    num = 0
    for c in s:
        num = num * 10 + chars[c]
    return num
