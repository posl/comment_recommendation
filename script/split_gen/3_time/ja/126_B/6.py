def main():
    s = input()
    yymm = int(s[:2]) <= 12 and int(s[2:]) <= 12
    mmyy = int(s[:2]) <= 12 and int(s[2:]) <= 12
    if yymm and mmyy:
        print("AMBIGUOUS")
    elif yymm:
        print("YYMM")
    elif mmyy:
        print("MMYY")
    else:
        print("NA")
