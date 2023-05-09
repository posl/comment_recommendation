def main():
    S = input()
    YY = S[:2]
    MM = S[2:]
    if int(YY) >= 1 and int(YY) <= 12:
        if int(MM) >= 1 and int(MM) <= 12:
            print("AMBIGUOUS")
        else:
            print("YYMM")
    elif int(MM) >= 1 and int(MM) <= 12:
        print("MMYY")
    else:
        print("NA")
