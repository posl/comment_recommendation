def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    def rotate(S):
        return list(zip(*S[::-1]))
    def check(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][j] == "#" and T[i][j] == ".":
                    return False
        return True
    for _ in range(4):
        if check(S, T):
            print("Yes")
            exit()
        S = rotate(S)
    print("No")
