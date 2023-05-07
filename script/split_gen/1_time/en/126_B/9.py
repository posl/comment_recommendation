def main():
    S = input()
    S = list(S)
    S1 = S[:2]
    S2 = S[2:]
    S1 = int("".join(S1))
    S2 = int("".join(S2))
    if (S1 < 13 and S1 > 0) and (S2 < 13 and S2 > 0):
        print("AMBIGUOUS")
    elif (S1 < 13 and S1 > 0) and (S2 >= 13 or S2 == 0):
        print("MMYY")
    elif (S1 >= 13 or S1 == 0) and (S2 < 13 and S2 > 0):
        print("YYMM")
    else:
        print("NA")
