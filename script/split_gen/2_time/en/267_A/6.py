def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if s == "Saturday" or s == "Sunday":
        print(0)
    else:
        print(week.index(s) - 5)
