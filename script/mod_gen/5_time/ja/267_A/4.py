def day_to_day(day):
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_num = day_list.index(day)
    return day_num
day = input()
day_num = day_to_day(day)
ans_num = 0

if __name__ == '__main__':
    day_to_day()