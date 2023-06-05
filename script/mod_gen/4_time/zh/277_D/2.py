def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 答えを格納する変数
    ans = 0
    # 余りを管理する配列
    count = [0] * M
    # 余りごとに数を数える
    for a in A:
        count[a % M] += 1
    # 余りが0のものは一枚だけ使える
    ans += count[0]
    # 余りがM/2のものも一枚だけ使える
    if M % 2 == 0:
        ans += 1
    # それ以外の余りの組み合わせを使う
    for i in range(1, M // 2 + 1):
        # 余りの大きいほうから使っていく
        j = M - i
        # 余りiのカードと余りjのカードを使う
        if count[i] > count[j]:
            ans += count[j]
            count[i] -= count[j]
            count[j] = 0
        else:
            ans += count[i]
            count[j] -= count[i]
            count[i] = 0
    # 余りが0のものが余った場合
    if count[0]:
        ans += count[0] - 1
    # 余りがM/2のものが余った場合
    if M % 2 == 0 and count[M // 2]:
        ans += count[M // 2] - 1
    # それ以外の余りの組み合わせが余った場合
    for i in range(1, M // 2 + 1):
        if count[i]:
            ans += count[i] - 1
    # 答えを出力する
    print(ans)

if __name__ == '__main__':
    main()