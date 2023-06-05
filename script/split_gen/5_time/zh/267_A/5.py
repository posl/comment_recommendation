def get_days_to_sat(s):
    days_to_sat = 0
    if s == '星期一':
        days_to_sat = 5
    elif s == '星期二':
        days_to_sat = 4
    elif s == '星期三':
        days_to_sat = 3
    elif s == '星期四':
        days_to_sat = 2
    elif s == '星期五':
        days_to_sat = 1
    return days_to_sat
