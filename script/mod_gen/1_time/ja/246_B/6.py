def main():
    # A,Bを取得
    A,B = map(int,input().split())
    # A,Bの最大公約数を取得
    gcd = GCD(A,B)
    # 最大公約数で割った時のA,Bの値を出力
    print(A/gcd,B/gcd)

if __name__ == '__main__':
    main()