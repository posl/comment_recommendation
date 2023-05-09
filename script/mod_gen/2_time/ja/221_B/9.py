def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        exit()
    for i in range(0, len(S)-1):
        S = S[:i]+S[i+1]+S[i]+S[i+2:]
        if S == T:
            print("Yes")
            exit()
        S = S[:i]+S[i+1]+S[i]+S[i+2:]
    print("No")
    exit()

if __name__ == '__main__':
    main()