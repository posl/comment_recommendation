def main():
    n, x = map(int, input().split())
    # 一文字目の文字コードを求める
    a = ord('A')
    # 一文字目の文字コードから x-1 文字目の文字コードを求める
    # 一文字目の文字コードから x-1 文字目の文字コードは (x-1) // n だけずれている
    # 一文字目の文字コードから x-1 文字目の文字コードの文字は chr(a+(x-1)//n) で求められる
    print(chr(a+(x-1)//n))
