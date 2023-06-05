def judge(s):
    if len(s) != 4 or not s.isupper():
        return False
    else:
        for i in range(4):
            if s.count(s[i]) != 2:
                return False
        return True
