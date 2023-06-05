def main():
    date = input()
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    if year < 2019:
        print("Heisei")
    elif year == 2019 and month < 4:
        print("Heisei")
    elif year == 2019 and month == 4 and day <= 30:
        print("Heisei")
    else:
        print("TBD")
