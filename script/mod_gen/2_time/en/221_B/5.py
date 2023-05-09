def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        S2 = S[:i] + S[i+1] + S[i] + S[i+2:]
        if S2 == T:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()