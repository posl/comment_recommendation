def get_days(s):
    days = 0
    for i in range(6):
        if s == 'Saturday':
            break
        elif s == 'Friday':
            days += 1
            s = 'Saturday'
        elif s == 'Thursday':
            days += 2
            s = 'Saturday'
        elif s == 'Wednesday':
            days += 3
            s = 'Saturday'
        elif s == 'Tuesday':
            days += 4
            s = 'Saturday'
        elif s == 'Monday':
            days += 5
            s = 'Saturday'
    return days
