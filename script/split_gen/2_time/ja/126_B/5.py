def main():
    S = input()
    if (int(S[2:4]) >= 1) and (int(S[2:4]) <= 12) and (int(S[0:2]) >= 1) and (int(S[0:2]) <= 12):
        print("AMBIGUOUS")
    elif (int(S[2:4]) >= 1) and (int(S[2:4]) <= 12):
        print("YYMM")
    elif (int(S[0:2]) >= 1) and (int(S[0:2]) <= 12):
        print("MMYY")
    else:
        print("NA")
