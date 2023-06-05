def check(s, t):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != t[i][j]:
                return False
    return True

if __name__ == '__main__':
    check()