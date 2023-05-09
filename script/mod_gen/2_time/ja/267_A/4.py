def solve():
    s = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i, day in enumerate(days):
        if s == day:
            print(6 - i)

if __name__ == '__main__':
    solve()