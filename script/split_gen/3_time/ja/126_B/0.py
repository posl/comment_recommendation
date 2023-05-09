def main():
    S = input()
    if S[0] == "0" and S[1] == "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] == "0" and S[3] != "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] != "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] == "0" and S[2] != "0" and S[3] != "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] == "0" and S[3] != "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] != "0" and S[3] == "0":
        print("NA")
    elif S[0] == "0" and S[1] != "0" and S[2] != "0" and S[3] != "0":
        if S[2] == "0" and S[3] == "0":
            print("NA")
        elif S[2] == "0" and S[3] != "0":
            print("NA")
        elif S[2] != "0" and S[3] == "0":
            print("NA")
        elif S[2] != "0" and S[3] != "0":
            print("YYMM")
    elif S[0] != "0" and S[1] == "0" and S[2] == "0" and S[3] == "0":
        print("NA")
    elif S[0] != "0" and S[1] == "0" and S[2
