def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = "No"
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j+1:]
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == ".":
                            S[k] = S[k][:l] + "#" + S[k][l+1:]
                            for m in range(N):
                                for n in range(N):
                                    if S[m][n] == "#":
                                        if m+5 < N:
                                            if S[m+1][n] == "#" and S[m+2][n] == "#" and S[m+3][n] == "#" and S[m+4][n] == "#" and S[m+5][n] == "#":
                                                ans = "Yes"
                                        if n+5 < N:
                                            if S[m][n+1] == "#" and S[m][n+2] == "#" and S[m][n+3] == "#" and S[m][n+4] == "#" and S[m][n+5] == "#":
                                                ans = "Yes"
                                        if m+5 < N and n+5 < N:
                                            if S[m+1][n+1] == "#" and S[m+2][n+2] == "#" and S[m+3][n+3] == "#" and S[m+4][n+4] == "#" and S[m+5][n+5] == "#":
                                                ans = "Yes"
                                        if m+5 < N and n-5 >= 0:
                                            if S[m+1][n-1] == "#" and S[m+2][n-2] == "#" and S[m+3][n-3] == "#" and S[m+4][n-4] == "#" and S[m+5][n-5] == "#":
                                                ans = "Yes"
                            S[k] = S[k][:l] + "." + S[k][l+1:]
                S[i] = S[i][:j] + "." + S[i][j+1:]
    print(ans)

if __name__ == '__main__':
    main()