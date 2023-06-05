def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    s = list(s)
    t = list(t)
    min_change = 1000
    for i in range(len_s - len_t + 1):
        change_cnt = 0
        for j in range(len_t):
            if t[j] != s[i + j]:
                change_cnt += 1
        min_change = min(min_change, change_cnt)
    print(min_change)
