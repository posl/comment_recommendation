def main():
    S = input()
    S = [int(i) for i in S]
    if S[0] == 0:
        if S[1] == 0:
            if S[2] == 0:
                print("NA")
            else:
                if S[3] == 0:
                    print("NA")
                else:
                    print("YYMM")
        else:
            if S[2] == 0:
                if S[3] == 0:
                    print("NA")
                else:
                    print("YYMM")
            else:
                if S[3] == 0:
                    print("NA")
                else:
                    print("YYMM")
    else:
        if S[1] == 0:
            if S[2] == 0:
                if S[3] == 0:
                    print("NA")
                else:
                    print("MMYY")
            else:
                if S[3] == 0:
                    print("NA")
                else:
                    print("MMYY")
        else:
            if S[2] == 0:
                if S[3] == 0:
                    print("NA")
                else:
                    print("MMYY")
            else:
                if S[3] == 0:
                    print("NA")
                else:
                    print("MMYY")
