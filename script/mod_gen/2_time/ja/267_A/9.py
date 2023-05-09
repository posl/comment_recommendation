def get_days(week):
    week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return week_list.index(week) + 1

if __name__ == '__main__':
    get_days()