def main():
    #入力
    n = int(input())
    x = list(map(int, input().split()))
    #処理
    ans = 10**9
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i)**2
        ans = min(ans, tmp)
    #出力
    print(ans)

if __name__ == '__main__':
    main()