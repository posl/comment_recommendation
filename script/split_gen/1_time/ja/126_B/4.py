def main():
    s = input()
    if int(s[0:2]) > 12 and int(s[2:4]) > 12:
        print("NA")
    elif int(s[0:2]) > 12 and int(s[2:4]) <= 12:
        print("YYMM")
    elif int(s[0:2]) <= 12 and int(s[2:4]) > 12:
        print("MMYY")
    else:
        print("AMBIGUOUS")
