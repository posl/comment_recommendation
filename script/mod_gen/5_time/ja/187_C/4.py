def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = "satisfiable"
    for i in range(N):
        if S[i][0] == "!":
            if S[i][1:] in S:
                ans = S[i][1:]
                break
        else:
            if "!" + S[i] in S:
                ans = S[i]
                break
    print(ans)

if __name__ == '__main__':
    main()