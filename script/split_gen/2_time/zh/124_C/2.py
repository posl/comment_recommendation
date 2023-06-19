def solve(s):
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    count = 0
    for i in range(1, len(s) - 1):
        if s[i - 1] == s[i] and s[i] == s[i + 1]:
            count += 1
            s[i] = '0' if s[i] == '1' else '1'
    if s[0] == s[1]:
        count += 1
    if s[len(s) - 1] == s[len(s) - 2]:
        count += 1
    return count
