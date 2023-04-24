Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for S in range(1 << N):
            for j in range(N):
                if (S >> j) & 1:
                    dp[i][S] = max(dp[i][S], dp[i - 1][S ^ (1 << j)] + A[i - 1][j])
    print(dp[N][(1 << N) - 1])

=======
Suggestion 2

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    ans = 0
    for i in range(2*N-1):
        for j in range(i+1, 2*N-1):
            ans ^= A[i][j-i-1]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [0] * (2 ** N)
    for i in range(2 ** N):
        for j in range(N):
            if ((i >> j) & 1):
                B[i] ^= A[j][i & ((1 << j) - 1)]
    dp = [0] * (2 ** N)
    for i in range(2 ** N):
        for j in range(2 ** N):
            if ((i & j) == 0):
                dp[i | j] = max(dp[i | j], dp[i] + B[j])
    print(dp[-1])

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    for i in range(2*N):
        A.append(list(map(int, input().split())))
    dp = [[0]*(2**N) for _ in range(2*N)]
    for i in range(2*N):
        for j in range(2*N):
            if i < j:
                dp[i][j] = A[i][j-1-i]
    for i in range(2*N):
        for j in range(2*N):
            if i < j:
                if (i & j) == 0:
                    dp[i][j] += dp[i][j^(i|j)]
    print(max(dp[i][j] for i in range(2*N) for j in range(2*N) if i < j))

=======
Suggestion 5

def read():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    return N, A

=======
Suggestion 6

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    #print(A)
    ans = 0
    for i in range(2*N-1):
        for j in range(i+1, 2*N):
            ans = ans ^ A[i][j-i-1]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(max([frozenset([i, j]) for i in range(N) for j in range(N)], key=lambda x: sum([A[i][j] for i, j in x])))

=======
Suggestion 8

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    # print(A)
    # print(A[1][2])
    # print(A[2][3])

    # 2N人の参加者がN個の2人組に分かれる方法
    # N個の2人組の相性がそれぞれB1, B2, ..., BN
    # とすると、舞踏会全体の楽しさはそれらのビットごとの排他的論理和である
    # B1 ⊕ B2 ⊕ ... ⊕ BN です。

    # 2N人の参加者がN個の2人組に分かれる方法
    # 2N人の参加者がN個の2人組に分かれる方法を自由に選べるとき、
    # 「舞踏会全体の楽しさ」としてあり得る最大値を出力してください。

    # 2人組の相性の最大値を求める
    max_val = 0
    for i in range(N):
        for j in range(i+1, N):
            max_val = max(max_val, A[i][j])

    # 2人組の相性の最大値のビット数を求める
    max_bit = 0
    while max_val > 0:
        max_val //= 2
        max_bit += 1

    # print(max_val)
    # print(max_bit)

    # 2人組の相性の最大値のビット数の桁数を求める
    # 2のmax_bit乗の桁数を求める
    max_digit = 0
    while 10**max_digit < 2**max_bit:
        max_digit += 1

    # print(max_digit)

    # 2人組の相性の最大値のビット数の桁数を求める
    # 2のmax_bit乗の桁数を

=======
Suggestion 9

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    #print(A)

    #N人をN組に分けるときの最大値を求める
    #2人組を構成する人のうち、番号の小さい方の人が人 i 、番号の大きい方の人が人 j のとき、
    #その 2 人組の「相性」は A_{i, j} です。
    #N 個の 2 人組の相性がそれぞれ B_1, B_2, ..., B_N であるとき、
    #「舞踏会全体の楽しさ」はそれらのビットごとの排他的論理和である B_1 ⊕ B_2 ⊕ ... ⊕ B_N です。
    #「 2N 人の参加者が N 個の 2 人組に分かれる方法」を自由に選べるとき、「舞踏会全体の楽しさ」としてあり得る最大値を出力してください。

    #N人をN組に分けるときの最大値を求める
    #2人組を構成する人のうち、番号の小さい方の人が人 i 、番号の大きい方の人が人 j のとき、
    #その 2 人組の「相性」は A_{i, j} です。
    #N 個の 2 人組の相性がそれぞれ B_1, B_2, ..., B_N であるとき、
    #「舞踏会全体の楽しさ」はそれらのビットごとの排他的論理和である B_1 ⊕ B_2 ⊕ ... ⊕ B_N です。
    #「 2N 人の参加者が N

=======
Suggestion 10

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(A)

    #2^N通りの2人組を作る
    #2人組の相性をBに格納
    B = []
    for i in range(2**N):
        #print(i)
        x = 0
        for j in range(N):
            if (i >> j) & 1:
                x = x ^ A[j][j+1]
        B.append(x)
    #print(B)

    #2人組の相性をビットごとに見ていく
    #2人組の相性のビットごとの排他的論理和を求める
    #最大値を出力
    ans = 0
    for i in range(30):
        #print(i)
        x = 0
        for j in range(2**N):
            if (B[j] >> i) & 1:
                x += 1
        ans = ans + max(x, 2**N - x) * 2**i
    print(ans)
