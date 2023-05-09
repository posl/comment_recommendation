def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = sorted(S)
    for i in range(N-1):
        if S[i][0] == "!" and S[i+1][0] == "!":
            continue
        if S[i][0] == "!" and S[i+1][0] != "!":
            S[i] = S[i][1:]
            if S[i] == S[i+1]:
                print(S[i])
                return
        if S[i][0] != "!" and S[i+1][0] == "!":
            S[i+1] = S[i+1][1:]
            if S[i] == S[i+1]:
                print(S[i])
                return
    print("satisfiable")

if __name__ == '__main__':
    main()