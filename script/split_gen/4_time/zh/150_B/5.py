def countABC(s):
    count = 0
    for i in range(len(s)-2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
            count += 1
    return count
