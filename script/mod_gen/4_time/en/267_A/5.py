def main():
    s = input()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(days.index('Saturday') - days.index(s))

if __name__ == '__main__':
    main()