def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    def rotate90(S):
        return ["".join([S[j][i] for j in range(N-1, -1, -1)]) for i in range(N)]
    def check(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][j] != T[i][j]:
                    return False
        return True
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                Sx, Sy = i, j
            if T[i][j] == "#":
                Tx, Ty = i, j
    for _ in range(4):
        S = rotate90(S)
        if check(S, T):
            print("Yes")
            exit()
    for dx in range(-N+1, N):
        for dy in range(-N+1, N):
            for _ in range(4):
                S = rotate90(S)
                if check(S, T):
                    print("Yes")
                    exit()
    print("No")
