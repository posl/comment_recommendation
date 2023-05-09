def main():
    S = input()
    year, month, day = S.split('/')
    if int(year) < 2019:
        print("Heisei")
    elif int(year) == 2019:
        if int(month) < 5:
            print("Heisei")
        elif int(month) == 5 and int(day) <= 31:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")

if __name__ == '__main__':
    main()