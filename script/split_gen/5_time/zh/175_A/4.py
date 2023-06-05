def max_rain_days(s):
    count = 0
    max_count = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count
