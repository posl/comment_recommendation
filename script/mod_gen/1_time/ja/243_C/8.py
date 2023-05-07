def main():
    # 入力
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(list(map(int, input().split())))
    S = input()
    # ここから書き始める
    # まずは左右の人の数を数える
    cnt_l = 0
    cnt_r = 0
    for i in range(N):
        if S[i] == 'L':
            cnt_l += 1
        else:
            cnt_r += 1
    # その後、左右の人の数が同じならば、衝突は発生しない
    if cnt_l == cnt_r:
        print('No')
        return
    # それ以外の場合、衝突は発生する
    print('Yes')

if __name__ == '__main__':
    main()