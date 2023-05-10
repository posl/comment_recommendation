def countSharp(s):
    c = 0
    for i in range(len(s)):
        if s[i] == 'v' and i < len(s) - 1 and s[i+1] == 'w':
            c += 1
    return c

if __name__ == '__main__':
    countSharp()