def main():
    L, Q = map(int, input().split())
    # 木材の長さを入れるリスト
    wood = [L]
    # クエリの処理
    for _ in range(Q):
        c, x = map(int, input().split())
        # 木材の切り分け
        if c == 1:
            wood.append(x)
            wood.append(L - x)
            wood.sort()
            L = wood[-1]
        # 木材の長さを出力
        else:
            for i in range(len(wood)):
                if wood[i] >= x:
                    print(wood[i])
                    break

if __name__ == '__main__':
    main()