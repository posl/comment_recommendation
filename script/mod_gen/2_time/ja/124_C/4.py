def main():
    # 入力
    S = input()
    # 処理
    N = len(S)
    count = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            count += 1
    # 出力
    print(count)

if __name__ == '__main__':
    main()