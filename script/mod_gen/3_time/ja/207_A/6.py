def main(): #main関数を定義
    A, B, C = map(int, input().split()) #map関数を使って、入力を整数に変換して、それぞれA,B,Cに代入
    print(max(A+B,A+C,B+C)) #max関数を使って、A+B,A+C,B+Cの中で最大の値を出力

if __name__ == '__main__':
    main()