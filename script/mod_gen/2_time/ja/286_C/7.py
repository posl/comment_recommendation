def main():
    N, A, B = map(int, input().split())
    S = input()
    # 1文字目と最後の文字が同じかどうか
    is_same = True
    for i in range(N // 2):
        if S[i] != S[N - 1 - i]:
            is_same = False
            break
    if is_same:
        # 同じならば、A円払っても回文にならない
        print(0)
        return
    # 1文字目と最後の文字が違うならば、A円払っても回文にならない
    # ただし、1文字目と最後の文字以外が全て同じならば、A円払っても回文にならない
    is_same_except_1st_and_last = True
    for i in range(1, N // 2):
        if S[i] != S[N - 1 - i]:
            is_same_except_1st_and_last = False
            break
    if is_same_except_1st_and_last:
        # 1文字目と最後の文字以外が全て同じならば、A円払っても回文にならない
        # ただし、1文字目と最後の文字以外が全て同じならば、B円払っても回文にならない
        is_same_except_1st_and_last = True
        for i in range(1, N // 2):
            if S[i] != S[N - 2 - i]:
                is_same_except_1st_and_last = False
                break
    if is_same_except_1st_and_last:
        # 1文字目と最後の文字以外が全て同じならば、B円払っても回文にならない
        # ただし、1文字目と最後の文字以外が全て同じならば、A円払っても回文にならない
        is_same_except_1st_and_last = True
        for i in range(1, N // 2):
            if S[i] != S[N

if __name__ == '__main__':
    main()