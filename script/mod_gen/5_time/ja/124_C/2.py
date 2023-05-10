def main():
    S = input()
    #print(S)
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    count = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == "1":
                count += 1
        else:
            if S[i] == "0":
                count += 1
    print(count)

if __name__ == '__main__':
    main()