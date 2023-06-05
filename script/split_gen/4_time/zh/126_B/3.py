def main():
    S = input()
    if S[0:2] >= "01" and S[0:2] <= "12" and S[2:4] >= "01" and S[2:4] <= "12":
        print("AMBIGUOUS")
    elif S[0:2] >= "01" and S[0:2] <= "12":
        print("MMYY")
    elif S[2:4] >= "01" and S[2:4] <= "12":
        print("YYMM")
    else:
        print("NA")
