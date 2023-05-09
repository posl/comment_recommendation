def main():
    # 標準入力から、K, A, B を取得
    K = int(input())
    A, B = map(int, input().split())
    # A 以上 B 以下の数値のリストを作成
    numbers = [i for i in range(A, B + 1)]
    # K の倍数のリストを作成
    multiples = [i for i in numbers if i % K == 0]
    # K の倍数のリストが空であれば NG を出力
    if not multiples:
        print('NG')
    # K の倍数のリストが空でなければ OK を出力
    else:
        print('OK')

if __name__ == '__main__':
    main()