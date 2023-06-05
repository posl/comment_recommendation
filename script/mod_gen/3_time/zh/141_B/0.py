def check_easy(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                continue
            else:
                return False
        else:
            if s[i] in ('R', 'U', 'D'):
                continue
            else:
                return False
    return True

if __name__ == '__main__':
    check_easy()