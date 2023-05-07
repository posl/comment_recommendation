def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                continue
            S[i] = S[i][:j] + "#" + S[i][j+1:]
            for k in range(N):
                if S[k][j] == "#":
                    continue
                S[k] = S[k][:j] + "#" + S[k][j+1:]
                if is_satisfied(S, N):
                    print("Yes")
                    return
                S[k] = S[k][:j] + "." + S[k][j+1:]
            S[i] = S[i][:j] + "." + S[i][j+1:]
    print("No")

if __name__ == '__main__':
    main()