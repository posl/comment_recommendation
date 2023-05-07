def main():
    N = int(input())
    # 2進数に変換
    binN = bin(N)[2:]
    # 2進数の桁数を取得
    lenN = len(binN)
    # 2進数の桁数分繰り返す
    for i in range(1, 2 ** lenN):
        # 2進数に変換
        binI = bin(i)[2:]
        # 2進数の桁数を取得
        lenI = len(binI)
        # 2進数の桁数が、2進数に変換したNの桁数より大きい場合
        if lenI > lenN:
            # 0を追加
            binN = '0' * (lenI - lenN) + binN
        # 2進数の桁数が、2進数に変換したNの桁数より小さい場合
        elif lenI < lenN:
            # 0を追加
            binI = '0' * (lenN - lenI) + binI
        # 2進数の桁数と、2進数に変換したNの桁数が同じ場合
        else:
            # 何もしない
            pass
        # 2進数の桁数分繰り返す
        for j in range(lenN):
            # 2進数に変換したNの桁数のうち、1が立っている桁数が、2進数に変換したiの桁数のうち、1が立っている桁数より大きい場合
            if binN.count('1') > binI.count('1'):
                # 2進数に変換したNの桁数のうち、1が立っている桁数が、2進数に変換したiの桁数のうち、1が立っている桁数より大
