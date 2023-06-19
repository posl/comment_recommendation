def main():
    s = input()
    a = int(s[0:2])
    b = int(s[2:4])
    if 0 < a < 13 and 0 < b < 13:
        print("AMBIGUOUS")
    elif 0 < a < 13 and 0 <= b < 100:
        print("MMYY")
    elif 0 <= a < 100 and 0 < b < 13:
        print("YYMM")
    else:
        print("NA")
