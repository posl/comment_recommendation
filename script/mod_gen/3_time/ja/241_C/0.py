def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j+1:]
                if check(S):
                    print("Yes")
                    return
                S[i] = S[i][:j] + "." + S[i][j+1:]
    print("No")

if __name__ == '__main__':
    main()