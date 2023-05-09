def main():
    S = input()
    if int(S[0:2]) >= 1 and int(S[0:2]) <= 12:
        if int(S[2:4]) >= 1 and int(S[2:4]) <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if int(S[2:4]) >= 1 and int(S[2:4]) <= 12:
            print("YYMM")
        else:
            print("NA")
