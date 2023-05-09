def is_multiple_of_8(s):
    if len(s) < 2:
        if int(s) % 8 == 0:
            return True
        else:
            return False
    elif len(s) == 2:
        if int(s) % 8 == 0:
            return True
        else:
            s = s[::-1]
            if int(s) % 8 == 0:
                return True
            else:
                return False
    else:
        s = list(s)
        s = [int(i) for i in s]
        s.sort()
        s = [str(i) for i in s]
        s = ''.join(s)
        if int(s) % 8 == 0:
            return True
        else:
            s = s[::-1]
            if int(s) % 8 == 0:
                return True
            else:
                return False
s = input()
