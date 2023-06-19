def main():
    day = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    week.reverse()
    print(week.index(day) + 1)
