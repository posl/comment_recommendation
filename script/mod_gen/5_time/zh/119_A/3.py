def main():
    import datetime
    s = input()
    y = int(s[:4])
    m = int(s[5:7])
    d = int(s[8:])
    if datetime.date(y, m, d) <= datetime.date(2019, 4, 30):
        print("Heisei")
    else:
        print("TBD")

if __name__ == '__main__':
    main()