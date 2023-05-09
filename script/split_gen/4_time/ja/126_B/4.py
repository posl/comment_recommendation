def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if (1 <= int(S1) <= 12) and (1 <= int(S2) <= 12):
        print("AMBIGUOUS")
    elif (1 <= int(S1) <= 12) and (13 <= int(S2) <= 99):
        print("MMYY")
    elif (13 <= int(S1) <= 99) and (1 <= int(S2) <= 12):
        print("YYMM")
    else:
        print("NA")
