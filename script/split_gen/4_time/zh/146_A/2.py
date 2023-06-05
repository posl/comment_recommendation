def get_next_sun_day(s):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return 7 - days.index(s)
