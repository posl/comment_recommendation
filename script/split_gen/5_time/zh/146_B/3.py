def move_str(s, n):
    if n == 0:
        return s
    else:
        res = ''
        for i in range(len(s)):
            tmp = ord(s[i]) + n
            if tmp > 90:
                tmp = tmp - 26
            res = res + chr(tmp)
        return res
