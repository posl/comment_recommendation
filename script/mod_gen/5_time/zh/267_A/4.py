def get_day_num(day):
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_num = day_list.index(day)
    return 7 - day_num

if __name__ == '__main__':
    get_day_num()