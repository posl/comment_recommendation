def check(s, t):
    for i in range(len(s)):
        if t == s[i:i+len(t)]:
            return True
    return False

if __name__ == '__main__':
    check()