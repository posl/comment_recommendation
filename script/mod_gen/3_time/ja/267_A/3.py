def main():
    S = input()
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(week.index("Saturday") - week.index(S) + 7)

if __name__ == '__main__':
    main()