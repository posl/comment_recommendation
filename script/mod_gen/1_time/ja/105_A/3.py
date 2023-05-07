def main():
    # 標準入力から数値を取得
    N, K = map(int, input().split())
    
    # 出力
    print(N % K)

if __name__ == '__main__':
    main()