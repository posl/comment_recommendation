def main():
    s = input()
    year, month, day = map(int, s.split('/'))
    if year < 2019:
        print("Heisei")
        return
    if year == 2019 and month <= 4:
        print("Heisei")
        return
    print("TBD")

if __name__ == '__main__':
    main()