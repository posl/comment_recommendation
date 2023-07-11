def judge_polygon(N, L):
    if max(L) < sum(L) - max(L):
        return "Yes"
    else:
        return "No"
