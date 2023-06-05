def judge(s):
    if len(s) == 1:
        if s == '8':
            return True
        else:
            return False
    elif len(s) == 2:
        if int(s) % 8 == 0:
            return True
        else:
            return False
    else:
        for i in range(112, 1000, 8):
            t = str(i)
            if len(t) == 2:
                t = '0' + t
            if t[0] in s and t[1] in s and t[2] in s:
                return True
        return False
s = input()
