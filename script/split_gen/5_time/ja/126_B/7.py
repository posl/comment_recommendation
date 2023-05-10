def main():
    S = input()
    if int(S[0:2]) > 12:
        if int(S[2:4]) > 12:
            print("NA")
        else:
            print("YYMM")
    else:
        if int(S[2:4]) > 12:
            print("MMYY")
        else:
            print("AMBIGUOUS")
