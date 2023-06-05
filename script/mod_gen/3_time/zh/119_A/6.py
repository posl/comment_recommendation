def main():
    s = input()
    ymd = s.split("/")
    if int(ymd[0]) < 2019:
        print("Heisei")
    elif int(ymd[0]) == 2019 and int(ymd[1]) < 4:
        print("Heisei")
    elif int(ymd[0]) == 2019 and int(ymd[1]) == 4 and int(ymd[2]) <= 30:
        print("Heisei")
    else:
        print("TBD")

if __name__ == '__main__':
    main()