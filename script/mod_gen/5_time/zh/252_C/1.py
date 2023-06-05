def check_same(s):
    for i in range(1, len(s)):
        if s[i] != s[0]:
            return False
    return True

if __name__ == '__main__':
    check_same()