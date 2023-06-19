def judge(s):
    if len(s) == 1:
        if s == "8":
            return True
        else:
            return False
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return True
        else:
            return False
    else:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in range(112, 1000, 8):
            t = str(i)
            dt = {}
            for j in t:
                if j in dt:
                    dt[j] += 1
                else:
                    dt[j] = 1
            if dt == d:
                return True
        return False
s = input()
