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

if __name__ == '__main__':
    main()