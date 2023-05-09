def main():
    # 3つの整数を入力
    A, B, C = map(int, input().split())
    # A,B,Cの合計値を出力
    print(A+B+C-max(A,B,C))

if __name__ == '__main__':
    main()