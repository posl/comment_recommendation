def main():
    day = input()
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day_list = day_list[day_list.index(day):] + day_list[:day_list.index(day)]
    print(day_list.index('Saturday') + 1)

if __name__ == '__main__':
    main()