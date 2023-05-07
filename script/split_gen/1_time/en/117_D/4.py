def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 2進数に変換してリストにする
    A_bin = [list(bin(i)[2:].zfill(40)) for i in A]
    # 2進数の桁ごとにXORした値を求める
    xor_sum = [0] * 40
    for i in range(40):
        xor_sum[i] = sum([int(a[i]) for a in A_bin]) % 2
    # 1が偶数個の場合は0になるので、1が奇数個の場合は1になる
    xor_sum = [str(1 - i) for i in xor_sum]
    xor_sum = int("".join(xor_sum), 2)
    # 2進数の桁ごとにXORした値とKを比較する
    # xor_sumの桁の値が1の場合、Kの桁の値は0にする
    # xor_sumの桁の値が0の場合、Kの桁の値は1にする
    K_bin = list(bin(K)[2:].zfill(40))
    for i in range(40):
        if xor_sum & (1 << i):
            K_bin[i] = "0"
    K_bin = "".join(K_bin)
    K_bin = int(K_bin, 2)
    # 2進数の桁ごとにXORした値とKを比較する
    # xor_sumの桁の値が1の場合、Kの桁の値は0にする
    # xor_sumの桁の値が0の場合、Kの桁の値は1にする
    ans = 0
    for i in range(40):
        if xor_sum & (1 << i):
            ans += (1 << i) * N
        else:
            ans += max((1 << i) * N - (1 << i) * sum([int(a[i]) for a in A_bin]), (1 << i) * sum
