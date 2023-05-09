def main():
    N, A, B = map(int, input().split())
    S = input()
    if N == 1:
        print(0)
        return
    # 総費用
    cost = 0
    # 現在の文字列
    now = S
    # 1文字ずつチェック
    for i in range(N//2):
        # 両端が同じなら何もしない
        if now[i] == now[N-1-i]:
            continue
        # 両端が異なるなら、A円払うかB円払うかを選択する
        else:
            # A円払う
            if A < B:
                cost += A
            # B円払う
            else:
                cost += B
    print(cost)

if __name__ == '__main__':
    main()