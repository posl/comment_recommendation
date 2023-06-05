def check(s, num):
    for i in range(0, 10):
        if s[i] == 'o' and str(i) not in num:
            return False
        if s[i] == 'x' and str(i) in num:
            return False
    return True

if __name__ == '__main__':
    check()