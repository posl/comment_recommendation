def moveN(n, s):
    res = ""
    for i in range(len(s)):
        t = ord(s[i]) + n
        if t > ord('Z'):
            t = t - ord('Z') + ord('A') - 1
        res = res + chr(t)
    print(res)
