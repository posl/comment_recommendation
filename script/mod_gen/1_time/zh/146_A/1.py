def get_days(s):
    days = {
        'SUN': 7,
        'MON': 6,
        'TUE': 5,
        'WED': 4,
        'THU': 3,
        'FRI': 2,
        'SAT': 1
    }
    return days[s]

if __name__ == '__main__':
    get_days()