def main():
    S = input()
    #print(S)
    #print(len(S))
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
    #print(S[10])
    count = 0
    for i in range(0, 10):
        if S[i] == 'o':
            count += 1
    if count > 4:
        print(0)
        exit()
    if count == 4:
        print(24)
        exit()
    if count == 3:
        print(36)
        exit()
    if count == 2:
        print(14)
        exit()
    if count == 1:
        print(1)
        exit()
    if count == 0:
        print(0)
        exit()

if __name__ == '__main__':
    main()