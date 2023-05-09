def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                Sx, Sy = i, j
            if T[i][j] == "#":
                Tx, Ty = i, j
    dx, dy = Tx - Sx, Ty - Sy
    for i in range(N):
        for j in range(N):
            if 0 <= i + dx < N and 0 <= j + dy < N:
                if S[i][j] != T[i + dx][j + dy]:
                    print("No")
                    return
    print("Yes")
