def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        exit()
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            if S[:i+1]+S[i]+S[i+1:] == T:
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    main()