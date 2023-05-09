def main():
    # 入力
    N = int(input())
    # N=1の時の例外処理
    if N == 1:
        print(1)
        return
    # リストの作成
    s = [1]
    # 処理
    for i in range(2, N + 1):
        s.append(i)
        s.extend(s)
    # 出力
    print(*s)

if __name__ == '__main__':
    main()