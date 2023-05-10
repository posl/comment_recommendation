Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def left_shift(s):
    return s[1:]+s[0]

=======
Suggestion 2

def main():
    s = input()
    s_len = len(s)
    s_min = s
    s_max = s
    for i in range(s_len):
        s = s[1:] + s[0]
        if s < s_min:
            s_min = s
        if s_max < s:
            s_max = s
    print(s_min)
    print(s_max)

=======
Suggestion 3

def move_right(s):
    return s[-1] + s[:-1]

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    S = input()
    Smin = S
    Smax = S
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S < Smin:
            Smin = S
        if S > Smax:
            Smax = S
    print(Smin)
    print(Smax)

=======
Suggestion 6

def main():
    S = input()
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
    print(S_min)
    print(S_max)

=======
Suggestion 7

def shift_left(s):
    return s[1:] + s[0]

=======
Suggestion 8

def main():
    S = input()
    print(min(S[1:] + S[0], S[-1] + S[:-1]))
    print(max(S[1:] + S[0], S[-1] + S[:-1]))
main()
