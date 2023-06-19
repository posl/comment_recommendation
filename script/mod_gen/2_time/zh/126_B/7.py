def main():
    S = input()
    #print(S)
    S1 = S[0:2]
    S2 = S[2:4]
    #print(S1)
    #print(S2)
    if(int(S1) > 12 and int(S2) > 12):
        print("NA")
    elif(int(S1) > 12 and int(S2) <= 12):
        print("YYMM")
    elif(int(S1) <= 12 and int(S2) > 12):
        print("MMYY")
    elif(int(S1) <= 12 and int(S2) <= 12):
        print("AMBIGUOUS")

if __name__ == '__main__':
    main()