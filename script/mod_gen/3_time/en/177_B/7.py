def check(s, t, i):
    for j in range(len(t)):
        if s[i + j] != t[j]:
            return False
    return True

if __name__ == '__main__':
    check()