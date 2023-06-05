def judge(s):
    if len(s) == 1:
        if s[0] == '8':
            return True
        else:
            return False
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return True
        else:
            return False
    else:
        for i in range(100, 1000):
            if i % 8 == 0:
                if s.count('0') >= str(i).count('0') and s.count('1') >= str(i).count('1') and s.count('2') >= str(i).count('2') and s.count('3') >= str(i).count('3') and s.count('4') >= str(i).count('4') and s.count('5') >= str(i).count('5') and s.count('6') >= str(i).count('6') and s.count('7') >= str(i).count('7') and s.count('8') >= str(i).count('8') and s.count('9') >= str(i).count('9'):
                    if str(i) in s:
                        return True
        return False
s = input()
