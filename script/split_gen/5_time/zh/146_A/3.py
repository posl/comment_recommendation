def main():
    s = input()
    day = 0
    if s == 'SUN':
        day = 7
    elif s == 'MON':
        day = 6
    elif s == 'TUE':
        day = 5
    elif s == 'WED':
        day = 4
    elif s == 'THU':
        day = 3
    elif s == 'FRI':
        day = 2
    elif s == 'SAT':
        day = 1
    print(day)
