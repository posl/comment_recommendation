def main():
    s = input()
    days = 0
    if s == 'Monday':
        days = 5
    elif s == 'Tuesday':
        days = 4
    elif s == 'Wednesday':
        days = 3
    elif s == 'Thursday':
        days = 2
    elif s == 'Friday':
        days = 1
    print(days)

if __name__ == '__main__':
    main()