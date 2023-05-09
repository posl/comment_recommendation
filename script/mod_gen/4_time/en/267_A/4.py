def main():
    day = input()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(days.index('Saturday') - days.index(day))

if __name__ == '__main__':
    main()