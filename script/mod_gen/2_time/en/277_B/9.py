def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    
    #print(S)
    ans = "Yes"
    for i in range(N):
        if S[i][0] not in ["H", "D", "C", "S"]:
            ans = "No"
        if S[i][1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            ans = "No"
        if S.count(S[i]) >= 2:
            ans = "No"
    print(ans)

if __name__ == '__main__':
    main()