def main():
    s = input()
    year, month, day = s.split("/")
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 2019:
        print("Heisei")
    elif year == 2019:
        if month <= 4:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")

if __name__ == '__main__':
    main()