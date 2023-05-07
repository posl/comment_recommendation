def main():
    s = input()
    ym = s[0:2]
    my = s[2:4]
    if ym == "00" or int(ym) > 12:
        ym = "00"
    if my == "00" or int(my) > 12:
        my = "00"
    if ym == "00" and my == "00":
        print("NA")
    elif ym == "00" or my == "00":
        print("MMYY" if my != "00" else "YYMM")
    else:
        print("AMBIGUOUS")

if __name__ == '__main__':
    main()