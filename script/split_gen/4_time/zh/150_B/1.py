def count_ABC(s):
    cnt = 0
    for i in range(len(s)-2):
        if s[i:i+3] == "ABC":
            cnt += 1
    return cnt
