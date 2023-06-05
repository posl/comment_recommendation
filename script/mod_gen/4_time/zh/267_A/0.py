def main():
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    s = input()
    if s == "saturday" or s == "sunday":
        print(0)
    else:
        print(5-week.index(s))

if __name__ == '__main__':
    main()