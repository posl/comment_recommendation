def get_days(s):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(len(days)):
        if s == days[i]:
            return 6 - i

if __name__ == '__main__':
    get_days()