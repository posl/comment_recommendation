def main():
    #入力
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    #ソート
    p.sort()
    #出力
    print(sum(p[0:K]))

if __name__ == '__main__':
    main()