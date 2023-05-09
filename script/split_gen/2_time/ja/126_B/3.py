def main():
    s = input()
    if (s[0] == "0" and s[1] == "0") or (s[2] == "0" and s[3] == "0"):
        print("NA")
    elif (s[0] == "0" and s[1] == "0") and (s[2] == "0" and s[3] == "0"):
        print("NA")
    elif (s[0] == "0" and s[1] == "0") and (s[2] == "0" and s[3] != "0"):
        print("MMYY")
    elif (s[0] == "0" and s[1] == "0") and (s[2] != "0" and s[3] == "0"):
        print("MMYY")
    elif (s[0] == "0" and s[1] == "0") and (s[2] != "0" and s[3] != "0"):
        print("MMYY")
    elif (s[0] != "0" and s[1] == "0") and (s[2] == "0" and s[3] == "0"):
        print("YYMM")
    elif (s[0] != "0" and s[1] == "0") and (s[2] == "0" and s[3] != "0"):
        print("MMYY")
    elif (s[0] != "0" and s[1] == "0") and (s[2] != "0" and s[3] == "0"):
        print("AMBIGUOUS")
    elif (s[0] != "0" and s[1] == "0") and (s[2] != "0" and s[3] != "0"):
        print("AMBIGUOUS")
    elif (s[0] != "0" and s[1] != "0") and (s[2] == "0" and s[3] == "0"):
        print("YYMM")
    elif (s[0] != "0" and s[1] != "0") and (s[2] == "0" and s[3] != "0"):
        print
