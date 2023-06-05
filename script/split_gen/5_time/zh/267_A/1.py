def main():
    weekday = input()
    weekday = weekday.upper()
    if weekday == 'MONDAY':
        print(5)
    elif weekday == 'TUESDAY':
        print(4)
    elif weekday == 'WEDNESDAY':
        print(3)
    elif weekday == 'THURSDAY':
        print(2)
    elif weekday == 'FRIDAY':
        print(1)
    else:
        print(0)
