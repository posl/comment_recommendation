def main():
    X, Y, A, B = map(int, input().split())
    # 経験値の最大値
    max_exp = 0
    # 現在の強さ
    now_str = X
    while now_str < Y:
        # カコモンジムに通う
        if now_str * A < now_str + B:
            now_str *= A
            max_exp += 1
        # AtCoderジムに通う
        else:
            now_str += B
            max_exp += 1
    # 進化しないようにする
    if now_str >= Y:
        max_exp -= 1
    print(max_exp)

if __name__ == '__main__':
    main()