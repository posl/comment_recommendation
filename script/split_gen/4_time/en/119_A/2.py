def main():
    s = input()
    year = int(s.split("/")[0])
    month = int(s.split("/")[1])
    day = int(s.split("/")[2])
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
