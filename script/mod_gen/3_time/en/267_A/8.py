def main():
    day = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    idx = days.index(day)
    if idx >= 5:
        print(7 - idx)
    else:
        print(6 - idx)

if __name__ == '__main__':
    main()