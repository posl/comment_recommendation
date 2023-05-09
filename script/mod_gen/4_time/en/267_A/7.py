def main():
    s = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week = week + week
    for i in range(7):
        if s == week[i]:
            print(7-i)
            break

if __name__ == '__main__':
    main()