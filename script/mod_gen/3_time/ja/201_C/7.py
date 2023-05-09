def main():
    S = input()
    #S = "oooo?xxxxx"
    #S = "o?oo?oxoxo"
    #S = "xxxxx?xxxo"
    #S = "o?o?oxoxo"
    #S = "o?o?oxoxo"
    #S = "o?o?oxoxo"
    if S[0] == "o" and S[1] == "o" and S[2] == "o" and S[3] == "o" and S[4] == "o" and S[5] == "o" and S[6] == "o" and S[7] == "o" and S[8] == "o" and S[9] == "o":
    #    print("0")
    #    return
    #print(S)
    #print(len(S))
    ans = 0
    for i in range(10000):
        #print(i)
        #print(str(i).zfill(4))
        #print(S[0])
        #print(S[1])
        #print(S[2])
        #print(S[3])
        #print(S[4])
        #print(S[5])
        #print(S[6])
        #print(S[7])
        #print(S[8])
        #print(S[9])
        if S[0] == "o" and str(i).zfill(4)[0] != "0":
            continue
        elif S[0] == "x" and str(i).zfill(4)[0] == "0":
            continue
        elif S[0] == "?" and str(i).zfill(4)[0] == "0":
            continue
        if S[1] == "o" and str(i).zfill(4)[1] != "0":
            continue
        elif S[1] == "x" and str(i).zfill(4)[1] == "0":
            continue
        elif S[1] == "?" and str(i).zfill(4)[1] == "0":
            continue
        if S[2] == "o" and str(i).zfill(4)[2] != "0":
            continue
        elif S[2] == "x" and str(i

if __name__ == '__main__':
    main()