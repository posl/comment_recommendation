Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(day.index('Saturday') - day.index(s))

=======
Suggestion 2

def main():
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    s = input()
    print(week.index('Saturday') - week.index(s))

=======
Suggestion 3

def main():
    s = input()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(7):
        if s == days[i]:
            print(7 - i)
            break

=======
Suggestion 4

def get_days(s):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(len(days)):
        if s == days[i]:
            return 6 - i

=======
Suggestion 5

def day_to_day(day):
    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_num = day_list.index(day)
    return day_num

day = input()
day_num = day_to_day(day)
ans_num = 0

=======
Suggestion 6

def get_days(day):
    days = {
        'Monday': 5,
        'Tuesday': 4,
        'Wednesday': 3,
        'Thursday': 2,
        'Friday': 1
    }
    return days[day]

=======
Suggestion 7

def day_to_int(day):
    if day == 'Monday':
        return 1
    elif day == 'Tuesday':
        return 2
    elif day == 'Wednesday':
        return 3
    elif day == 'Thursday':
        return 4
    elif day == 'Friday':
        return 5
    elif day == 'Saturday':
        return 6
    elif day == 'Sunday':
        return 7

=======
Suggestion 8

def get_next_day(day):
    if day == 'Sunday':
        next_day = 'Monday'
    elif day == 'Monday':
        next_day = 'Tuesday'
    elif day == 'Tuesday':
        next_day = 'Wednesday'
    elif day == 'Wednesday':
        next_day = 'Thursday'
    elif day == 'Thursday':
        next_day = 'Friday'
    elif day == 'Friday':
        next_day = 'Saturday'
    elif day == 'Saturday':
        next_day = 'Sunday'
    return next_day

=======
Suggestion 9

def main():
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    s = input()
    print(5 - week.index(s))
