def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    def rotate(S):
        return ["".join(S[i][j] for i in range(N)) for j in range(N-1,-1,-1)]
    def translate(S, x, y):
        return [S[i][j] for i in range(N) for j in range(N) if 0 <= i+y < N and 0 <= j+x < N]
    def check(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][j] == "#" and T[i][j] == "#":
                    return True
        return False
    for i in range(-N+1, N):
        for j in range(-N+1, N):
            for _ in range(4):
                S = rotate(S)
                if check(translate(S, i, j), T):
                    print("Yes")
                    return
    print("No")
main()
