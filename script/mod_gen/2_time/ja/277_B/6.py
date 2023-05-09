def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3] or S[3] == S[4] or S[4] == S[5]:
        print("No")
        return
    for i in range(N):
        if S[i][0] != "H" and S[i][0] != "D" and S[i][0] != "C" and S[i][0] != "S":
            print("No")
            return
        if S[i][1] != "A" and S[i][1] != "2" and S[i][1] != "3" and S[i][1] != "4" and S[i][1] != "5" and S[i][1] != "6" and S[i][1] != "7" and S[i][1] != "8" and S[i][1] != "9" and S[i][1] != "T" and S[i][1] != "J" and S[i][1] != "Q" and S[i][1] != "K":
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()