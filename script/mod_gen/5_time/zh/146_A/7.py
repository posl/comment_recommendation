def main():
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    day = 7
    s = input()
    print(day - week.index(s))

if __name__ == '__main__':
    main()