def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    if S1 == "H" or S1 == "2B" or S1 == "3B" or S1 == "HR":
        if S2 == "H" or S2 == "2B" or S2 == "3B" or S2 == "HR":
            if S3 == "H" or S3 == "2B" or S3 == "3B" or S3 == "HR":
                if S4 == "H" or S4 == "2B" or S4 == "3B" or S4 == "HR":
                    if S1 != S2 and S1 != S3 and S1 != S4 and S2 != S3 and S2 != S4 and S3 != S4:
                        print("Yes")
                    else:
                        print("No")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
