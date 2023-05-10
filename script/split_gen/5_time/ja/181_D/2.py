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
        for i in range(112, 1000, 8):
            a = list(str(i))
            b = list(s)
            for j in range(3):
                if a[j] in b:
                    b.remove(a[j])
                else:
                    break
            else:
                return True
        return False
s = input()
