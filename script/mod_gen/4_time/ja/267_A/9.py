def main():
    day = input()
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    print(week.index("Saturday") - week.index(day))

if __name__ == '__main__':
    main()