def solve():
    # === 数値変換 ===
    # N = int(input())
    # A, B = map(int, input().split())
    S = input()
    # K = int(input())
    # T = input()
    # === 行列入力 ===
    # A = [list(map(int, input().split())) for _ in range(N)]
    # === 行列計算 ===
    # A = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         A[i][j] = i * j
    # print(A)
    # === 行列出力 ===
    # for a in A:
    #     print(*a)
    T = S
    for i in range(len(S)):
        T = T[-1] + T[:-1]
        if S > T:
            S = T
    T = S
    for i in range(len(S)):
        T = T[1:] + T[0]
        if S > T:
            S = T
    print(S)
    T = S
    for i in range(len(S)):
        T = T[-1] + T[:-1]
        if S < T:
            S = T
    T = S
    for i in range(len(S)):
        T = T[1:] + T[0]
        if S < T:
            S = T
    print(S)

if __name__ == '__main__':
    solve()