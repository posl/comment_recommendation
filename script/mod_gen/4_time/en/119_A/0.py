def main():
    s = input()
    y = int(s[0:4])
    m = int(s[5:7])
    d = int(s[8:10])
    if y < 2019:
        print("Heisei")
    elif y == 2019:
        if m < 4:
            print("Heisei")
        elif m == 4:
            if d <= 30:
                print("Heisei")
            else:
                print("TBD")
        else:
            print("TBD")
    else:
        print("TBD")

if __name__ == '__main__':
    main()