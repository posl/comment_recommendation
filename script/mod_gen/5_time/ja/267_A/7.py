def get_next_day(day):
    if day == 'Sunday':
        next_day = 'Monday'
    elif day == 'Monday':
        next_day = 'Tuesday'
    elif day == 'Tuesday':
        next_day = 'Wednesday'
    elif day == 'Wednesday':
        next_day = 'Thursday'
    elif day == 'Thursday':
        next_day = 'Friday'
    elif day == 'Friday':
        next_day = 'Saturday'
    elif day == 'Saturday':
        next_day = 'Sunday'
    return next_day

if __name__ == '__main__':
    get_next_day()