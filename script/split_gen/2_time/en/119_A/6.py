def main():
    date = input()
    #print(date)
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    #print(year)
    #print(month)
    #print(day)
    if year <= 2019:
        if month <= 4:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")
