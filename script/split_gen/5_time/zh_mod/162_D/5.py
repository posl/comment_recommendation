def get_num(s):
    l = len(s)
    num = 0
    for i in range(l-2):
        for j in range(i+1, l-1):
            k = j + j - i
            if k < l:
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    num += 1
