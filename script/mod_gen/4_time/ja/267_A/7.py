def get_days(s):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days.index("Saturday") - days.index(s)
print(get_days(input()))
