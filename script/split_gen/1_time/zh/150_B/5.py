def count_abc(s):
    count = 0
    for i in range(0,len(s)-2):
        if s[i:i+3] == 'ABC':
            count += 1
    return count
