def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                S[i] = S[i][:j] + "." + S[i][j+1:]
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j+1:]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                S[i] = S[i][:j] + "." + S[i][j+1:]
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j+1:]
    ans = "No"
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                if i + 5 < N and j + 5 < N:
                    if S[i+1][j+1] == "#" and S[i+2][j+2] == "#" and S[i+3][j+3] == "#" and S[i+4][j+4] == "#" and S[i+5][j+5] == "#":
                        ans = "Yes"
                        break
                if i + 5 < N:
                    if S[i+1][j] == "#" and S[i+2][j] == "#" and S[i+3][j] == "#" and S[i+4][j] == "#" and S[i+5][j] == "#":
                        ans = "Yes"
                        break
                if j + 5 < N:
                    if S[i][j+1] == "#" and S[i][j+2] == "#" and S[i][j+3] == "#" and S[i][j+4] == "#" and S[i][j+5] == "#":
                        ans = "Yes"
                        break
    print(ans)

if __name__ == '__main__':
    main()