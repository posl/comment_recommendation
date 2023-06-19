def main():
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    week = week + week
    s = input()
    print(week.index('Saturday') - week.index(s) + 1)

if __name__ == '__main__':
    main()