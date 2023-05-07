def main():
    # 入力
    N, A, B = map(int, input().split())
    S = input()
    # 処理
    ans = 0
    for i in range(N):
        if S[i] == S[N-i-1]:
            continue
        else:
            ans += min(A, B)
    # 出力
    print(ans)

if __name__ == '__main__':
    main()