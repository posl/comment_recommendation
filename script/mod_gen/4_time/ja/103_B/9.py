def main():
    S = input()
    T = input()
    #print(S, T)
    if S == T:
        print("Yes")
        exit()
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()