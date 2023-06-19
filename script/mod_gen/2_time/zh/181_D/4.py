def main():
    S = input()
    if len(S) == 1:
        if S == '8':
            print("是")
        else:
            print("否")
        return
    if len(S) == 2:
        if int(S)%8 == 0 or int(S[1]+S[0])%8 == 0:
            print("是")
        else:
            print("否")
        return
    if len(S) == 3:
        if int(S)%8 == 0 or int(S[2]+S[0]+S[1])%8 == 0 or int(S[1]+S[2]+S[0])%8 == 0 or int(S[2]+S[1]+S[0])%8 == 0 or int(S[1]+S[0]+S[2])%8 == 0:
            print("是")
        else:
            print("否")
        return
    if len(S) == 4:
        if int(S)%8 == 0 or int(S[3]+S[0]+S[1]+S[2])%8 == 0 or int(S[2]+S[3]+S[0]+S[1])%8 == 0 or int(S[1]+S[2]+S[3]+S[0])%8 == 0 or int(S[0]+S[1]+S[2]+S[3])%8 == 0 or int(S[3]+S[2]+S[1]+S[0])%8 == 0 or int(S[2]+S[1]+S[0]+S[3])%8 == 0 or int(S[1]+S[0]+S[3]+S[2])%8 == 0:
            print("是")
        else:
            print("否")
        return
    if len(S) == 5:
        if int(S)%8 == 0 or int(S[4]+S[0]+S[1]+S[2]+S[3])%8 == 0 or int(S[3]+S[4]+S[0]+S[1]+S[2])%8 == 0 or int(S[2]+S[3]+S[4]+S[0]+S[1])%8 == 0 or int(S[1

if __name__ == '__main__':
    main()