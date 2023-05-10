def rotateString(s,t):
    for i in range(len(s)):
        if s == t:
            return True
        else:
            s = s[-1] + s[:-1]
    return False

if __name__ == '__main__':
    rotateString()