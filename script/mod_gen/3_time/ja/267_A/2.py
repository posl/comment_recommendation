def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(week.index("Saturday") - week.index(s))

if __name__ == '__main__':
    main()