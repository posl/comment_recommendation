def main():
    S = input()
    a = S[0:2]
    b = S[2:4]
    if 1 <= int(a) <= 12 and 1 <= int(b) <= 12:
        print("AMBIGUOUS")
    elif 1 <= int(a) <= 12 and (int(b) == 0 or int(b) > 12):
        print("MMYY")
    elif (int(a) == 0 or int(a) > 12) and 1 <= int(b) <= 12:
        print("YYMM")
    else:
        print("NA")
