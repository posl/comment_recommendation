def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S = [S_1, S_2, S_3]
    S.sort()
    if S[0] == "ABC" and S[1] == "AGC":
        print("ARC")
    elif S[0] == "ABC" and S[1] == "AHC":
        print("AGC")
    elif S[0] == "AGC" and S[1] == "ARC":
        print("ABC")
    elif S[0] == "AGC" and S[1] == "AHC":
        print("ARC")
    elif S[0] == "ARC" and S[1] == "AHC":
        print("AGC")
    elif S[0] == "ARC" and S[1] == "ABC":
        print("AGC")
    elif S[0] == "AHC" and S[1] == "ABC":
        print("ARC")
    elif S[0] == "AHC" and S[1] == "ARC":
        print("AGC")
