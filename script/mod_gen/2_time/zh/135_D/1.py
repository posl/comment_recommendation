def solve(s):
    #print(s)
    if len(s) == 1:
        if s[0] == '?':
            return 5
        else:
            return 1
    elif len(s) == 2:
        if s[0] == '?' and s[1] == '?':
            return 25
        elif s[0] == '?' and s[1] != '?':
            return 2
        elif s[0] != '?' and s[1] == '?':
            if int(s[0]) % 13 == 5:
                return 1
            else:
                return 0
        else:
            if int(s) % 13 == 5:
                return 1
            else:
                return 0
    elif len(s) == 3:
        if s[0] == '?' and s[1] == '?' and s[2] == '?':
            return 125
        elif s[0] == '?' and s[1] == '?' and s[2] != '?':
            return 10
        elif s[0] == '?' and s[1] != '?' and s[2] == '?':
            return 10
        elif s[0] == '?' and s[1] != '?' and s[2] != '?':
            if int(s[1] + s[2]) % 13 == 5:
                return 2
            else:
                return 0
        elif s[0] != '?' and s[1] == '?' and s[2] == '?':
            if int(s[0] + '0') % 13 == 5:
                return 10
            else:
                return 0
        elif s[0] != '?' and s[1] == '?' and s[2] != '?':
            if int(s[0] + s[2]) % 13 == 5:
                return 2
            else:
                return 0
        elif s[0] != '?' and s[1] != '?' and s[2] == '?':
            if int(s[0] + s[1]) % 13 == 5:
                return 2
            else:
                return 0
        else:
            if int(s) % 13 == 5:
                return 1
            else:
                return 0

if __name__ == '__main__':
    solve()