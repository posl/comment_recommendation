def check(s):
    for i in range(len(s)):
        if s.count(s[i]) > 1:
            return False
    return True

if __name__ == '__main__':
    check()