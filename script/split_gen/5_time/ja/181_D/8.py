def check(s):
    if len(s) == 1:
        return s == "8"
    elif len(s) == 2:
        return int(s) % 8 == 0 or int(s[::-1]) % 8 == 0
    else:
        c = [0] * 10
        for ss in s:
            c[int(ss)] += 1
        for i in range(112, 1000, 8):
            if not c[i // 100] >= 1:
                continue
            if not c[i // 10 % 10] >= 1:
                continue
            if not c[i % 10] >= 1:
                continue
            return True
        return False
s = input()
