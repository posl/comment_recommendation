def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    # 2進数表記での桁数を求める
    bit_length = len(bin(max(K, max(As)))) - 2
    # 桁ごとに考える
    # 2進数表記での桁数分繰り返す
    for i in range(bit_length):
        # 2進数表記でi桁目が立っている数を求める
        mask = 1 << (bit_length - i - 1)
        # 2進数表記でi桁目が立っている数のうち、K以下のものの数を求める
        count = sum([1 for A in As if A & mask])
        # 2進数表記でi桁目が立っている数のうち、K以下のものの数がN/2より大きければ、
        # その桁は全て1になる
        if count > N // 2:
            # 2進数表記でi桁目が立っている数のうち、K以下のものの数がN/2より大きい場合、
            # その桁は全て1になるので、その桁の数値を加算する
            K += mask
    # 各桁をXORした値の総和の最大値を求める
    print(sum([A ^ K for A in As]))

if __name__ == '__main__':
    main()