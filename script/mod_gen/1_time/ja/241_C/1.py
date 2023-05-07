def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j + 1:]
                if six(S):
                    print("Yes")
                    return
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == ".":
                            S[k] = S[k][:l] + "#" + S[k][l + 1:]
                            if six(S):
                                print("Yes")
                                return
                            S[k] = S[k][:l] + "." + S[k][l + 1:]
                S[i] = S[i][:j] + "." + S[i][j + 1:]
    print("No")

if __name__ == '__main__':
    main()