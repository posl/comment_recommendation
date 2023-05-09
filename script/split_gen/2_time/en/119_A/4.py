def main():
    date = input()
    y, m, d = date.split('/')
    if int(y) < 2019:
        print("Heisei")
    elif int(y) == 2019:
        if int(m) < 5:
            print("Heisei")
        elif int(m) == 4:
            if int(d) < 31:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")
