def main():
    day = input()
    dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(dayList.index("Saturday") - dayList.index(day) + 1)

if __name__ == '__main__':
    main()