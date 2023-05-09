def main():
    # 入力
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # 処理
    ans = 0
    for i in range(1, N):
        if S[i] != S[i-1]:
            ans += 1
    # 出力
    print(ans+1)

if __name__ == '__main__':
    main()