def war_or_peace(N, M, X, Y, x_list, y_list):
    for Z in range(X + 1, Y + 1):
        if max(x_list) < Z and min(y_list) >= Z:
            return '无战争'
    return '战争'
