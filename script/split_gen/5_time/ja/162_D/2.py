def solve():
    N = int(input())
    S = input()
    # R, G, B の個数を数える
    R = S.count('R')
    G = S.count('G')
    B = S.count('B')
    # まずは、同じ文字の組を数える
    ans = R * G * B
    # 以下、異なる文字の組を数える
    # i, j, k を全探索する
    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i
            if k >= N:
                continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)
