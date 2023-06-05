def get_day_index(day):
    day_index = 0
    if day == 'SUN':
        day_index = 0
    elif day == 'MON':
        day_index = 1
    elif day == 'TUE':
        day_index = 2
    elif day == 'WED':
        day_index = 3
    elif day == 'THU':
        day_index = 4
    elif day == 'FRI':
        day_index = 5
    elif day == 'SAT':
        day_index = 6
    return day_index
