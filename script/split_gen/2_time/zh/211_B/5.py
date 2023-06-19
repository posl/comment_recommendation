def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    if S_1 == "H" or S_2 == "H" or S_3 == "H" or S_4 == "H":
        if S_1 == "2B" or S_2 == "2B" or S_3 == "2B" or S_4 == "2B":
            if S_1 == "3B" or S_2 == "3B" or S_3 == "3B" or S_4 == "3B":
                if S_1 == "HR" or S_2 == "HR" or S_3 == "HR" or S_4 == "HR":
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
main()
