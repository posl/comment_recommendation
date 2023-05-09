def check(s, t):
    if len(s) < len(t):
        return False
    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j]:
                break
        else:
            return True
    return False
s = input()
t = input()

if __name__ == '__main__':
    check()