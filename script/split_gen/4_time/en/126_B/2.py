def main():
    s = input()
    if int(s[2:4]) <= 12 and int(s[2:4]) > 0 and int(s[0:2]) <= 12 and int(s[0:2]) > 0:
        print("AMBIGUOUS")
    elif int(s[2:4]) <= 12 and int(s[2:4]) > 0:
        print("YYMM")
    elif int(s[0:2]) <= 12 and int(s[0:2]) > 0:
        print("MMYY")
    else:
        print("NA")
