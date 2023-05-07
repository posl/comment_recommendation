def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i][j] = "#"
                if check(S, N):
                    print("Yes")
                    return
                S[i][j] = "."
    print("No")
