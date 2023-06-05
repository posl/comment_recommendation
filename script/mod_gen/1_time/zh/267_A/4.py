def main():
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = input()
    print(5 - weekdays.index(day) if weekdays.index(day) < 5 else 7 - weekdays.index(day))

if __name__ == '__main__':
    main()