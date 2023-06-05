def main():
    # 変数a,b,c,dを取得する
    a,b,c,d = map(int,input().split())
    # (a+b)×(c-d)を計算する
    ans = (a+b)*(c-d)
    # 結果を出力する
    print(ans)
    print("Takahashi")

if __name__ == '__main__':
    main()