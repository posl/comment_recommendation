def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # kの2進数表記の桁数
    k_len = len(bin(k)[2:])
    # aの2進数表記の桁数がkより大きい場合は、
    # aの最上位k_len桁を捨てる
    a = [ai >> max(0, len(bin(ai)[2:]) - k_len) for ai in a]
    # aの各桁の1の個数を数える
    a_count = [0] * k_len
    for ai in a:
        for i in range(k_len):
            a_count[i] += ai >> i & 1
    # a_countの各桁の1の個数を数える
    a_count_count = [0] * k_len
    for ai in a_count:
        for i in range(k_len):
            a_count_count[i] += ai >> i & 1
    # fの各桁の1の個数を数える
    f_count = [0] * k_len
    for i in range(k_len):
        f_count[i] = (a_count_count[i] * (n - a_count_count[i]) << i)
    # fの10進数表記を求める
    f = 0
    for i in range(k_len):
        f += f_count[i] << i
    print(f)
