def main():
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    s = input()
    print(week.index('Saturday') - week.index(s))

if __name__ == '__main__':
    main()