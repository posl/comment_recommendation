def slime(s):
    if len(s) == 1:
        return 1
    else:
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                break
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                i = 0
            else:
                i += 1
        return len(s)

if __name__ == '__main__':
    slime()