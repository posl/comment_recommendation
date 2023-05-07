def main():
    # Get input
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    
    # Check if we have one of each of H, 2B, 3B, and HR
    if (S_1 == "H" or S_2 == "H" or S_3 == "H" or S_4 == "H") and (S_1 == "2B" or S_2 == "2B" or S_3 == "2B" or S_4 == "2B") and (S_1 == "3B" or S_2 == "3B" or S_3 == "3B" or S_4 == "3B") and (S_1 == "HR" or S_2 == "HR" or S_3 == "HR" or S_4 == "HR"):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()