def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[len(S)-len(T)+i:]
        ans = "Yes"
        for j in range(len(T)):
            if T[j] == "?":
                continue
            if S1[j] == "?" or S2[j] == "?":
                continue
            if S1[j] != T[j] and S2[j] != T[j]:
                ans = "No"
                break
        print(ans)

if __name__ == '__main__':
    main()