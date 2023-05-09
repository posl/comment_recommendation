def get_days(s):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days.index("Saturday") - days.index(s)
print(get_days(input()))

if __name__ == '__main__':
    get_days()