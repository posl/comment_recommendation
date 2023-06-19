def main():
    S = input()
    S = list(S)
    #print(S)
    for i in range(len(S)):
        S[i] = int(S[i])
    #print(S)
    S.sort()
    #print(S)
    if len(S) == 1:
        if S[0] == 8:
            print("Yes")
        else:
            print("No")
        return
    if len(S) == 2:
        if (S[0]*10 + S[1]) % 8 == 0 or (S[1]*10 + S[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    if len(S) == 3:
        if (S[0]*100 + S[1]*10 + S[2]) % 8 == 0 or (S[0]*100 + S[2]*10 + S[1]) % 8 == 0 or (S[1]*100 + S[0]*10 + S[2]) % 8 == 0 or (S[1]*100 + S[2]*10 + S[0]) % 8 == 0 or (S[2]*100 + S[0]*10 + S[1]) % 8 == 0 or (S[2]*100 + S[1]*10 + S[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    if len(S) == 4:
        if (S[0]*1000 + S[1]*100 + S[2]*10 + S[3]) % 8 == 0 or (S[0]*1000 + S[1]*100 + S[3]*10 + S[2]) % 8 == 0 or (S[0]*1000 + S[2]*100 + S[1]*10 + S[3]) % 8 == 0 or (S[0]*1000 + S[2]*100 + S[3]*10 + S[1]) % 8 == 0 or (S[0]*1000 + S[3]*100 + S[1]*10 + S[2]) % 8 == 0 or (S[0]*1000 + S[3]*100 + S[

if __name__ == '__main__':
    main()