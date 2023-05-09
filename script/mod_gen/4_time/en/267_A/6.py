def main():
    s = input().strip()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(6 - days.index(s))

if __name__ == '__main__':
    main()