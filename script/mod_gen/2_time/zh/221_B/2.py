def check(s,t):
    if s == t:
        return True
    else:
        for i in range(len(s)-1):
            if s[i+1] == t[i] and s[i] == t[i+1]:
                return True
        return False

if __name__ == '__main__':
    check()