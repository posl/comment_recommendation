def check(s):
    for i in range(10):
        if s[i] == 'o':
            if str(i) not in s:
                return False
        elif s[i] == 'x':
            if str(i) in s:
                return False
    return True

if __name__ == '__main__':
    check()