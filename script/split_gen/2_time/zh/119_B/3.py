def main():
    #input
    date = input()
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    #compute
    if year < 2019:
        print("Heisei")
    elif year == 2019:
        if month < 4:
            print("Heisei")
        elif month == 4:
            if day <= 30:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")
main()
