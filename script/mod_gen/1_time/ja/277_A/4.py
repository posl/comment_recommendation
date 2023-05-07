def main():
    #入力
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    #処理
    for i in range(N):
        if P[i] == X:
            ans = i + 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()