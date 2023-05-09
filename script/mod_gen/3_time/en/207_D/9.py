def match_point(n, s, t):
    for i in range(n):
        for j in range(n):
            if s[i][0] == t[j][0] and s[i][1] == t[j][1]:
                s[i][0] = 0
                t[j][0] = 0
                s[i][1] = 0
                t[j][1] = 0
                break
    return s, t

if __name__ == '__main__':
    match_point()