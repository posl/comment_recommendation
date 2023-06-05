def getNum(s):
    res = 0
    for i in range(len(s)):
        res = res * 26 + ord(s[i]) - ord('A') + 1
    return res

if __name__ == '__main__':
    getNum()