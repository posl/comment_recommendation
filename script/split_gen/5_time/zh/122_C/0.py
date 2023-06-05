def countAC(s, l, r):
    count = 0
    for i in range(l, r):
        if s[i] == 'A' and s[i+1] == 'C':
            count += 1
    return count
