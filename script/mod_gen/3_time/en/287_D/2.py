def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        for j in range(len(T)):
            if S1[j] == T[j] or S1[j] == '?':
                continue
            else:
                print("No")
                break
        else:
            for j in range(len(T)):
                if S2[j] == T[j] or S2[j] == '?':
                    continue
                else:
                    print("No")
                    break
            else:
                print("Yes")
    return

if __name__ == '__main__':
    main()