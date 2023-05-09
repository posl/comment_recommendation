def get_next_sunday(s):
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return 7 - day.index(s)
