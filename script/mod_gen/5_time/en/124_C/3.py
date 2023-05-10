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
    count = 0
    for i in range(len(S)):
        #print(S[i])
        if i % 2 == 0:
            if S[i] == '1':
                count += 1
        else:
            if S[i] == '0':
                count += 1
    print(count)

if __name__ == '__main__':
    main()