def countAC(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] == 'C':
            count += 1
    return count
