def main():
    S = input()
    S_list = S.split("/")
    S_year = int(S_list[0])
    S_month = int(S_list[1])
    S_day = int(S_list[2])
    if S_year < 2019:
        print("Heisei")
    elif S_year == 2019:
        if S_month < 4:
            print("Heisei")
        elif S_month == 4:
            if S_day <= 30:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")
