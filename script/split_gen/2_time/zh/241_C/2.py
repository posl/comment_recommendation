def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        S[i] = S[i].replace(".", "0")
        S[i] = S[i].replace("#", "1")
        S[i] = list(map(int, S[i]))
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                S[i][j] = 0
            else:
                S[i][j] = 1
    for i in range(N):
        S[i] = S[i][::-1]
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                S[i][j] = 0
            else:
                S[i][j] = 1
    for i in range(N):
        S[i] = S[i][::-1]
    for i in range(N):
        S[i] = S[i][::-1]
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                S[i][j] = 0
            else:
                S[i][j] = 1
    for i in range(N):
        S[i] = S[i][::-1]
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                S[i][j] = 0
            else:
                S[i][j] = 1
    for i in range(N):
        S[i] = S[i][::-1]
    for i in range(N):
        S[i] = S[i][::-1]
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                S[i][j] = 0
            else:
                S[i][j] = 1
    for i in range(N):
        S[i] = S[i][::-1]
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                S[i][j] = 0
            else:
                S[i][j] = 1
    for i in range(N):
        S[i] = S[i][::-1]
    for
