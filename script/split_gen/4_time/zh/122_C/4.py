def count_ac(s):
    cnt = 0
    for i in range(len(s) - 1):
        if s[i] == 'A' and s[i + 1] == 'C':
            cnt += 1
    return cnt
