def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if S1 == "00" or S1 == "01" or S1 == "02" or S1 == "03" or S1 == "04" or S1 == "05" or S1 == "06" or S1 == "07" or S1 == "08" or S1 == "09" or S1 == "10" or S1 == "11" or S1 == "12":
        if S2 == "00" or S2 == "01" or S2 == "02" or S2 == "03" or S2 == "04" or S2 == "05" or S2 == "06" or S2 == "07" or S2 == "08" or S2 == "09" or S2 == "10" or S2 == "11" or S2 == "12":
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if S2 == "00" or S2 == "01" or S2 == "02" or S2 == "03" or S2 == "04" or S2 == "05" or S2 == "06" or S2 == "07" or S2 == "08" or S2 == "09" or S2 == "10" or S2 == "11" or S2 == "12":
            print("YYMM")
        else:
            print("NA")
