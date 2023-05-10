def main():
    s = input()
    s = s.split("/")
    if int(s[0]) < 2019:
        print("Heisei")
    elif int(s[0]) == 2019:
        if int(s[1]) < 5:
            print("Heisei")
        elif int(s[1]) == 5:
            if int(s[2]) <= 30:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")

if __name__ == '__main__':
    main()