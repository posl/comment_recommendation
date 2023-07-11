def judge_polygon(n, l):
    l_max = max(l)
    l_sum = sum(l) - l_max
    if l_max < l_sum:
        return
