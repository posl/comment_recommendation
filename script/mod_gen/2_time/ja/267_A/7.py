def get_days(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return 7 - days.index(day)

if __name__ == '__main__':
    get_days()