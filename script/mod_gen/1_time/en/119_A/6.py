def main():
    S = input()
    year = int(S[:4])
    month = int(S[5:7])
    day = int(S[-2:])
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