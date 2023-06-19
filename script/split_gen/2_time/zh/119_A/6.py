def main():
    s=input()
    year=int(s[:4])
    month=int(s[5:7])
    day=int(s[8:])
    if year<2019:
        print("Heisei")
    elif year==2019:
        if month<=4:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")
