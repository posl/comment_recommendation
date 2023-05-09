def main():
    #入力
    N = int(input())
    d = [int(x) for x in input().split()]
    #ソート
    d.sort()
    #切り出し
    d = d[N//2:]
    #出力
    print(d[0] - d[-1] + 1)

if __name__ == '__main__':
    main()