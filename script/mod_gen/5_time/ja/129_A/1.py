def main():
    # データ入力
    p,q,r = map(int,input().split())
    # 出力
    print(min(p+q,q+r,r+p))

if __name__ == '__main__':
    main()