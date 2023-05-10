def main():
    S = input()
    S = S[::-1]
    S = S + "0"
    S = S + "0"
    S = S + "0"
    S = S + "0"
    S = S + "0"
    ans = 0
    for i in range(len(S)-5):
        if S[i] == "0":
            ans += 1
        elif S[i] == "1":
            ans += 2
        elif S[i] == "2":
            ans += 3
        elif S[i] == "3":
            ans += 4
        elif S[i] == "4":
            ans += 5
        elif S[i] == "5":
            ans += 6
        elif S[i] == "6":
            ans += 7
        elif S[i] == "7":
            ans += 8
        elif S[i] == "8":
            ans += 9
        elif S[i] == "9":
            ans += 10
    print(ans)
main()
