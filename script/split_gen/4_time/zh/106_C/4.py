def problem106_c(s, k):
    s = list(s)
    for i in range(10):
        s = [str(i) if x == str(i) else x for x in s]
        s = [x * (i + 1) if x == str(i) else x for x in s]
    s = ''.join(s)
    print(s[k - 1])
