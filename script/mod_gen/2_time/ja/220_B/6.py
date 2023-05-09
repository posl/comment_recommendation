def main():
    # 入力
    K = int(input())
    A, B = map(str, input().split())
    # 処理
    A10 = int(A, K)
    B10 = int(B, K)
    # 出力
    print(A10 * B10)

if __name__ == '__main__':
    main()