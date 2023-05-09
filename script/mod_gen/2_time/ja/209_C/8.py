def main():
    #入力
    N = int(input())
    C = list(map(int, input().split()))
    #初期値
    ans = 1
    mod = 10**9+7
    #処理
    for i in range(N-1):
        if C[i] == C[i+1]:
            ans *= 2
            ans %= mod
        elif C[i] > C[i+1]:
            ans *= 1
            ans %= mod
        else:
            ans *= 2
            ans %= mod
            if C[i] == C[i+1]-1:
                ans *= 1
                ans %= mod
            else:
                ans *= 0
                ans %= mod
    #出力
    print(ans)

if __name__ == '__main__':
    main()