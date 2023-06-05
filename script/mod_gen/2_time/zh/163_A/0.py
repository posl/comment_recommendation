def count(s):
    c = [0]*3
    for i in range(len(s)):
        if s[i] == 'R':
            c[0] += 1
        elif s[i] == 'G':
            c[1] += 1
        else:
            c[2] += 1
    return c[0]*c[1]*c[2]

if __name__ == '__main__':
    count()