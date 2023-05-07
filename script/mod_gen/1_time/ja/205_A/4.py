def main():
    # 標準入力から A B を取得する。
    A, B = map(int, input().split())
    # A の値で割った値を B にかけて出力する。
    print(A / 100 * B)

if __name__ == '__main__':
    main()