def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    lenS = len(S)
    #print(lenS)
    lenT = len(T)
    #print(lenT)
    if lenS != lenT:
        print("No")
        exit()
    for i in range(lenS):
        if S[i] != T[i]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()