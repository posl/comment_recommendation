def check_login_days(n, login_days):
    login_days.sort()
    days = [0] * n
    for i in range(n):
        for j in range(i, n):
            if login_days[i] <= login_days[j] < login_days[i] + n:
                days[j - i] += 1
            else:
                break
    return days
