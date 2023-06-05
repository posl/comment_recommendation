def solve(s):
    #print(s)
    if len(s) <= 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    count = 0
    if s[0] == s[1]:
        if s[0] == '0':
            count += 1
            s = '1' + s[1:]
        else:
            count += 1
            s = '0' + s[1:]
    for i in range(1, len(s) - 1):
        if s[i] == s[i + 1]:
            if s[i] == '0':
                count += 1
                s = s[:i + 1] + '1' + s[i + 2:]
            else:
                count += 1
                s = s[:i + 1] + '0' + s[i + 2:]
    if s[-1] == s[-2]:
        if s[-1] == '0':
            count += 1
            s = s[:-1] + '1'
        else:
            count += 1
            s = s[:-1] + '0'
    #print(s)
    return count + solve(s)
