def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                sy, sx = i, j
            if T[i][j] == "#":
                ty, tx = i, j
    for i in range(4):
        S = list(zip(*S[::-1]))
        for j in range(N):
            for k in range(N):
                if S[j][k] == "#":
                    sy, sx = j, k
        if sy == ty and sx == tx:
            print("Yes")
            return
    print("No")
