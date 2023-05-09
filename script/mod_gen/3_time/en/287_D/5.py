def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        if S1.count("?") + S2.count("?") + T.count("?") == len(S1) + len(S2) + len(T):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()