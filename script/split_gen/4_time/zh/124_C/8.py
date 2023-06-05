def solve(s):
    if len(s) == 1:
        return 0
    else:
        count = 0
        if s[0] == s[1]:
            count += 1
            if s[0] == '0':
                s[0] = '1'
            else:
                s[0] = '0'
        for i in range(1, len(s)-1):
            if s[i] == s[i+1] or s[i] == s[i-1]:
                count += 1
                if s[i] == '0':
                    s[i] = '1'
                else:
                    s[i] = '0'
        if s[-1] == s[-2]:
            count += 1
            if s[-1] == '0':
                s[-1] = '1'
            else:
                s[-1] = '0'
        return count
