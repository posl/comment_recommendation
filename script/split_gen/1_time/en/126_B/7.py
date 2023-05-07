def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if int(S1) > 0 and int(S1) < 13:
        if int(S2) > 0 and int(S2) < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if int(S2) > 0 and int(S2) < 13:
            print("YYMM")
        else:
            print("NA")
