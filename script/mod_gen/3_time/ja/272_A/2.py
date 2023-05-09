def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #処理
    ans = sum(A)
    #出力
    print(ans)

if __name__ == '__main__':
    main()