def main():
    # 入力
    K = int(input())
    A,B = map(int,input().split())
    # 10進数に変換
    A10 = int(str(A),K)
    B10 = int(str(B),K)
    # 出力
    print(A10*B10)

if __name__ == '__main__':
    main()