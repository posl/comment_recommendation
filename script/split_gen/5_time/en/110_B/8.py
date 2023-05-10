def war_or_no_war(N, M, X, Y, x, y):
    # x_max = max(x)
    # y_min = min(y)
    # if x_max < y_min:
    #     return "No War"
    # else:
    #     return "War"
    if max(x) < min(y) and X < min(y) and min(y) <= Y:
        return "No War"
    else:
        return "War"
