def main():
    s = input()
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(day.index('Saturday') - day.index(s))

if __name__ == '__main__':
    main()