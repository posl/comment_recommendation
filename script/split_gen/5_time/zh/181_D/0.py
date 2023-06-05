def is8(s):
    if len(s) == 1:
        if s == '8':
            return True
        else:
            return False
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return True
        else:
            return False
    if len(s) >= 3:
        for i in range(100,1000):
            if i % 8 == 0:
                flag = True
                for j in str(i):
                    if j not in s:
                        flag = False
                        break
                if flag:
                    return True
        return False
    return False
