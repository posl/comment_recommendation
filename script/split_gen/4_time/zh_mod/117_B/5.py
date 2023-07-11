def judge_polygon(n, l):
    max_len = max(l)
    l.remove(max_len)
    sum_len = sum(l)
    if max_len < sum_len:
        print("
