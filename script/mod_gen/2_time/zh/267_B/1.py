def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = input()
    index = days.index(day)
    if index < 5:
        print(5 - index)
    else:
        print(7 - index + 5)

if __name__ == '__main__':
    main()