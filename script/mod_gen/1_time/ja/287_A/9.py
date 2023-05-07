def main():
    # 入力
    N = int(input())
    S = [input() for _ in range(N)]
    # 計算
    # Forの数を数える
    count = 0
    for i in range(N):
        if S[i] == 'For':
            count += 1
    # 出力
    if count > N // 2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()