def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    def rotate(S):
        return ["".join(row) for row in zip(*S[::-1])]
    def translate(S, dx, dy):
        return [row[dx:] for row in S[dy:]]
    def check(S, T):
        for dx in range(N):
            for dy in range(N):
                if S == translate(T, dx, dy):
                    return True
        return False
    for _ in range(4):
        if check(S, T):
            print("Yes")
            return
        S = rotate(S)
    print("No")
