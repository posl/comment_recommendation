def find_num(s):
    s = s.split()
    n = int(s[0])
    s = s[1:]
    count = 1
    for i in range(1, n):
        if int(s[i]) < int(s[i - 1]):
            count += 1
    return count
