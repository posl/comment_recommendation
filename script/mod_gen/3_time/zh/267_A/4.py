def get_days_of_week(week_day):
    week_days = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    return week_days.index(week_day)+1

if __name__ == '__main__':
    get_days_of_week()