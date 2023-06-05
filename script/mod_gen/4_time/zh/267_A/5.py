def get_days_to_saturday(day):
    days = 0
    if day == 'Monday':
        days = 5
    if day == 'Tuesday':
        days = 4
    if day == 'Wednesday':
        days = 3
    if day == 'Thursday':
        days = 2
    if day == 'Friday':
        days = 1
    return days

if __name__ == '__main__':
    get_days_to_saturday()