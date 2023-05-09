def main():
    #入力
    N = int(input())
    H = list(map(int, input().split()))
    #最大値のインデックスを取得
    ans = H.index(max(H))
    #出力
    print(ans+1)

if __name__ == '__main__':
    main()